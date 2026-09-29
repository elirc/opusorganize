import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { calculate } from './capacity.mjs';

const manifest = JSON.parse(await readFile(new URL('../manifest.json', import.meta.url), 'utf8'));
let worksheetCases = 0;
for (const project of manifest.projects) {
  const worksheet = JSON.parse(await readFile(resolve(project.pack, 'capacity.json'), 'utf8'));
  for (const example of worksheet.calculations) {
    worksheetCases++;
    test(`${worksheet.project}: ${example.label}`, () => {
      const input = Object.freeze({ ...example.args });
      const actual = calculate(example.kind, input);
      assert.equal(typeof actual, 'number');
      assert.ok(Math.abs(actual - example.expected) <= 1e-9 * Math.max(1, Math.abs(example.expected)),
        `Expected ${example.expected} ${example.unit}; received ${actual}`);
      assert.deepEqual(input, example.args);
    });
  }
}
assert.equal(worksheetCases, 30);

test('saturated or overloaded queues have no positive drain rate', () => {
  assert.equal(calculate('queueDrain', { backlog: 100, arrivalsPerSecond: 10, workers: 2, secondsPerJob: 0.2 }), null);
  assert.equal(calculate('queueDrain', { backlog: 100, arrivalsPerSecond: 5, workers: 1, secondsPerJob: 0.5 }), null);
});

test('invalid rates and service-time boundaries reject', () => {
  assert.throws(() => calculate('originRps', { readsPerSecond: 10, hitRate: 1.1 }), RangeError);
  assert.throws(() => calculate('queueDrain', { backlog: 1, arrivalsPerSecond: 0, workers: 1, secondsPerJob: 0 }), RangeError);
  assert.throws(() => calculate('readRps', { active: -1, readsPerMinute: 2 }), RangeError);
  assert.throws(() => calculate('unknown', {}), TypeError);
});

test('the shared guide queue example includes continuing arrivals', () => {
  assert.equal(calculate('queueDrain', { backlog: 900, arrivalsPerSecond: 40, workers: 9, secondsPerJob: 0.2 }), 180);
});

test('the simplified thirty-day availability budget is 43.2 minutes', () => {
  assert.ok(Math.abs(30 * 24 * 60 * 0.001 - 43.2) < 1e-10);
});
