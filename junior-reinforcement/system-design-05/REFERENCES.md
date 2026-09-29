# Selected primary references and source boundaries

Reviewed 2026-09-28. The project packs link their inspected local source directly. The references below support selected general semantics; they are not recommendations to upgrade packages or adopt a cloud product.

- [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html): use when explaining the interaction between statements, concurrent writes, isolation choices, and retries.
- [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html): use when reviewing which rule a key, uniqueness boundary, check, or relationship actually enforces.
- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html): use when designing evidence for a proposed index or query change; inspect the execution behavior of the chosen command.
- [Transactional outbox guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html): use to examine the database/message dual-write window and repeated-delivery handling. No AWS deployment is proposed by linking this pattern explanation.

The worked architectures, API sketches, hypothetical loads, decision records, and exercises are original teaching designs grounded in the local projects. Exact endpoint names or entity fields in a proposed table should not be read as a deployment inventory. Historical application verification remains attributed to its original source record.

No external reference supplies a production throughput or hiring-readiness claim for these projects. Those claims would need their own measurements or assessment. The offline calculator verifies only the stated arithmetic.
