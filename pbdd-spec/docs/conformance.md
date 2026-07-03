# Conformance

A conforming PBDD runtime must:

1. Read `pbdd.yaml`.
2. Validate brain state against the declared schema version.
3. Apply only valid workflow transitions.
4. Preserve existing brain and artifact history unless an explicit event
   supersedes it.
5. Record decisions that affect future behavior.

A conforming starter project must:

1. Include a valid `pbdd.yaml`.
2. Include a `brain/` directory.
3. Include an `artifacts/` directory.
4. Avoid embedding runtime-specific implementation details in project state.

