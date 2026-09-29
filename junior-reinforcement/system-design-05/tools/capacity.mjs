function nonnegative(value) {
  if (!Number.isFinite(value) || value < 0) throw new RangeError('Expected a finite nonnegative value');
  return value;
}

export function calculate(kind, input) {
  for (const value of Object.values(input)) nonnegative(value);
  const n = key => nonnegative(input[key]);
  let result;
  switch (kind) {
    case 'readRps':
      result = n('active') * n('readsPerMinute') / 60;
      break;
    case 'writeRps':
      result = n('active') * n('writesPerHour') / 3600;
      break;
    case 'originRps': {
      const hitRate = n('hitRate');
      if (hitRate > 1) throw new RangeError('Hit rate must be between zero and one');
      result = n('readsPerSecond') * (1 - hitRate);
      break;
    }
    case 'storageGB':
      result = n('writesPerSecond') * n('bytesPerWrite') * 86400 * n('days') / 1e9;
      break;
    case 'queueDrain': {
      const backlog = n('backlog');
      const workers = n('workers');
      const secondsPerJob = n('secondsPerJob');
      if (!Number.isSafeInteger(workers) || workers < 1 || secondsPerJob === 0) {
        throw new RangeError('Workers must be a positive integer and service time must be positive');
      }
      const spareCapacity = workers / secondsPerJob - n('arrivalsPerSecond');
      if (spareCapacity <= 0) return null;
      result = backlog / spareCapacity;
      break;
    }
    case 'fanout':
      result = n('updatesPerSecond') * n('subscribers') * n('payloadBytes');
      break;
    case 'inFlight':
      result = n('requestsPerSecond') * n('meanSeconds');
      break;
    default:
      throw new TypeError('Unknown teaching calculation');
  }
  if (!Number.isFinite(result)) throw new RangeError('Result exceeds finite numeric representation');
  return result;
}
