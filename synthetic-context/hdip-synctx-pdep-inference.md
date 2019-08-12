---
id: hdip-synctx-pdep-inference
title: HDIP SYNCTX Inference in PDEP
sidebar_label: HDIP © SYNCTX Inference
---

# 📘 DPFI SYNCTX Resolution & Compilation Rules

---

# 1. Purpose

This specification defines how the **HDIP Data Product Factory & Intelligence capability (DPFI)** resolves, compiles, versions and validates a **Synthetic Context (SYNCTX)** from declarative PDEP artifacts and authoritative enterprise references.

Although the established term **inference** is retained, DPFI inference is deliberately constrained:

> **DPFI may discover candidates, but it MUST NOT manufacture Product identity, semantic relationships, Data authority, policy authority, joinability, or synthetic-generation obligations from weak evidence.**

DPFI therefore acts primarily as a **governed resolver and compiler**.

```text
PDEP declarative artifacts
        +
authoritative Product / Data / policy state
        |
        v
      DPFI
resolution + compilation
        |
        v
      SYNCTX
versioned relational /
constraint projection
```

SYNCTX compilation is distinct from both synthetic-generation execution and Product constitution:

```text
SYNCTX compilation
      !=
synthetic-generation execution
      !=
Product constitution
```

---

# 2. Authority and Semantic Boundaries

DPFI MUST preserve the authority boundaries of the specifications and enterprise authorities it consumes.

```text
BPS / PIN
  -> generic Product and Product Version semantics

GEDRM / GEDRA
  -> Data semantics and Data architectural authority

enterprise/domain semantic authorities
  -> canonical business meaning and relationships

schema / Data Contract authorities
  -> governed structural and interface bindings

policy / control authorities
  -> authoritative policy and control obligations

HDIP SYNCTX
  -> compiled synthetic-generation context projection
```

The following non-equivalences are normative:

```text
candidate dependency != SYNCTX membership

dependency path != direct membership

semantic relationship != technical join binding

matching field names != foreign key

privacy obligation != synthetic-generation requirement

synthetic output != Product automatically

SYNCTX != GEAIRM AI Context
```

---

# 3. Inputs to the Resolution / Compilation Process

The canonical PDEP inputs remain:

```text
IntentRecord (IR)
SemanticDescriptor (SD / DPROD draft)
PolicyIntent (PI)
BusinessAssertions (BA)
UsageContract (UC)
ProductDependencies (PD)
```

DPFI MAY additionally resolve authoritative state needed to compile those inputs, including:

```text
Product and Product Version registry state
Product classification references
schema and Data Contract versions
enterprise/domain ontology references
dependency and provenance references
policy / control obligations
currentness and lifecycle state
approved synthetic-generation request / strategy
quality and evaluation requirements
```

The PDEP artifacts express Product intent and design. They do not replace the underlying authorities referenced during compilation.

---

# 4. Output

The output of this process is a versioned **SYNCTX graph/projection** conforming to the HDIP SYNCTX ontology.

At minimum, where applicable, a compiled SYNCTX may contain:

```text
SYNCTX identity and version
member Product Version references
purpose reference
validated RelationshipBindings
ConstraintProjections
generationModeRef
fidelityLevelRef
request / initiative context
platform application reference
lifecycle / currentness state
```

A SYNCTX does **not** need to contain generated data or Product identities for future outputs.

---

# 5. Core Compilation Model

Conceptually:

```text
SYNCTX = Compile(
    IR,
    SD,
    PI,
    BA,
    UC,
    PD,
    AuthoritativeState,
    CompilerRuleSet
)
```

Where:

- `Compile` is deterministic with respect to normalized authoritative inputs and compiler/rule-set version;
- candidate discovery is distinct from governed acceptance;
- unresolved material ambiguity is surfaced rather than silently guessed;
- output is a graph/projection, not an independently authoritative replacement for its source semantics.

---

# 6. Seven Compilation Phases

DPFI executes SYNCTX resolution and compilation in **seven ordered logical phases**.

These are logical compiler phases. They do not require seven deployed services or seven synchronous runtime calls.

---

## 🔹 Phase 1 — Synthetic-Generation Applicability Resolution

### Objective

Determine whether the Product development context requires, selects, or permits a SYNCTX-backed synthetic-generation strategy.

### Rule 1.1 — No Purpose-Only Synthetic Requirement

```text
A purpose value by itself MUST NOT establish:
synthetic_required = TRUE
```

Purposes such as:

```text
model training
external sharing
testing
simulation
sandbox use
```

may be relevant evidence, but none universally requires synthetic data.

### Rule 1.2 — Resolve Applicability from Governed Evidence

DPFI MUST determine synthetic-generation applicability using the applicable combination of:

```text
Intent Record
Usage Contract / governed purpose
explicit Product design choice
policy / privacy obligations
Data Contract constraints
consumer requirements
approved synthetic-generation strategy
quality / evaluation requirements
```

The logical outcome SHOULD be one of:

```text
REQUIRED
SELECTED
NOT_APPLICABLE
INDETERMINATE
```

`REQUIRED` means an authoritative obligation or approved design requires synthetic generation.

`SELECTED` means synthetic generation is an approved realization choice even though other strategies may have been possible.

`NOT_APPLICABLE` means no SYNCTX-backed synthetic generation is required for the Product realization under compilation.

`INDETERMINATE` means material evidence is missing or contradictory.

### Rule 1.3 — Privacy Does Not Imply Synthetic Generation

```text
privacy obligation
    !=
synthetic-generation requirement
```

Privacy or disclosure obligations may be realized through controls such as:

```text
minimisation
masking
tokenisation
anonymisation
aggregation
access restriction
purpose limitation
synthetic generation
or combinations of controls
```

DPFI MUST NOT infer a synthetic-generation requirement solely from terms such as `no_pii`, `masking_required`, or equivalent privacy constraints.

### Rule 1.4 — SYNCTX May Be Single-Member or Multi-Member

A SYNCTX MAY contain one or more member Product Versions.

```text
member count > 1
    != prerequisite for SYNCTX
```

A single Product Version may still require a SYNCTX to express generation purpose, constraints, fidelity, scenario rules or other generation requirements.

### Phase 1 Result

```text
IF applicability = NOT_APPLICABLE
THEN skip SYNCTX compilation

IF applicability = REQUIRED or SELECTED
THEN proceed

IF applicability = INDETERMINATE
THEN stop or escalate according to PDEP governance
```

---

## 🔹 Phase 2 — Member Product-Version Resolution

### Objective

Resolve the specific Product Versions whose governed state materially participates in the synthetic-generation context.

### Rule 2.1 — Membership Is Product-Version-Specific

```text
SYNCTX members = applicable Product Versions
```

DPFI MUST NOT bind only an enduring Product identity where the compiled schema, semantics, Data Contract or constraints are version-dependent.

### Rule 2.2 — Direct Dependencies Are Candidates, Not Automatic Members

Declared Product dependencies MAY establish candidate members.

A candidate becomes a SYNCTX member only where its governed state materially participates in the synthetic-generation context.

### Rule 2.3 — No Automatic Transitive Expansion

DPFI MAY inspect upstream dependency paths for candidate discovery, but MUST NOT automatically include every transitive upstream dependency as a direct SYNCTX member.

```text
A depends on B
B depends on C

DOES NOT imply
C is automatically a direct SYNCTX member for A
```

An upstream Product Version may instead remain only a dependency or provenance reference if it does not directly participate in the generation context.

### Rule 2.4 — Version Resolution Must Be Explicit

For each accepted member, DPFI MUST resolve an applicable Product Version according to governed Product/dependency/currentness rules.

```text
latest version != automatically governed current version
```

If the required Product Version cannot be resolved unambiguously, compilation MUST NOT silently choose one.

### Rule 2.5 — Deduplicate by Stable Product-Version Identity

```text
MemberVersions = unique(ProductVersion identities)
```

Deduplication MUST NOT collapse distinct versions of the same Product into one identity.

### Phase 2 Result

```text
MemberVersions = ResolveApplicableMemberVersions(
    PD,
    ProductVersionState,
    Purpose,
    GenerationRequirements
)
```

---

## 🔹 Phase 3 — Relationship-Binding Resolution

### Objective

Resolve the semantic and/or technical relationships that must be preserved or represented across member Product Versions.

### Rule 3.1 — Authoritative Semantic Relationships May Be Projected

Where the authoritative semantic descriptor or ontology establishes an applicable relationship, DPFI MAY project it as:

```text
synctx:semanticRelationshipRef
```

within a validated `synctx:RelationshipBinding`.

The semantic relationship alone does not establish a technical join.

### Rule 3.2 — Technical Join/Key Bindings Require Governed Evidence

A technical binding MUST be supported by applicable authoritative evidence such as:

```text
schema metadata
Data Contract
key / identifier semantics
referential-integrity rule
approved mapping
validated transformation specification
```

Where present, DPFI MAY project the technical binding through:

```text
synctx:joinBindingRef
```

### Rule 3.3 — Matching Names Are Candidate Evidence Only

```text
same attribute name
same datatype
similar identifiers
```

MAY aid discovery, but MUST NOT independently establish:

```text
foreign key
semantic equivalence
referential integrity
joinability
```

### Rule 3.4 — Ontology Relationship Does Not Automatically Create an Executable Join

```text
semantic relationship
    !=
technical join binding
```

DPFI MUST keep these dimensions separately traceable.

### Rule 3.5 — Referential Integrity Is Requirement-Driven

A relationship MUST NOT automatically imply preservation of referential integrity.

Referential-integrity preservation is required only where supported by the applicable Data Contract, key semantics, generation requirement, business assertion or other governed constraint.

### Rule 3.6 — Relationship Conflicts Require Governed Resolution

Where candidate relationship evidence conflicts, DPFI MUST apply explicit authoritative precedence/resolution rules if available.

If a material conflict remains unresolved:

```text
RelationshipBinding = INDETERMINATE
Compilation = FAIL / ESCALATE
```

according to applicable PDEP governance.

### Phase 3 Result

```text
RelationshipBindings = ResolveValidatedRelationships(
    MemberVersions,
    SD,
    EnterpriseSemantics,
    Schemas,
    DataContracts,
    BusinessAssertions
)
```

---

## 🔹 Phase 4 — Generation-Requirement Resolution

### Objective

Resolve the generation requirements that SYNCTX must project without hard-coding universal purpose-to-mode or purpose-to-fidelity rules.

### Rule 4.1 — Generation Mode Is Requirement-Driven

DPFI MUST NOT infer generation mode solely from relationship count.

Generation mode may depend on:

```text
validated RelationshipBindings
temporal-consistency requirements
shared scenario variables
business assertions
common population constraints
policy constraints
quality / evaluation requirements
consumer purpose
```

Where a governed generation mode is resolved, SYNCTX SHOULD reference it through:

```text
synctx:generationModeRef
```

### Rule 4.2 — Fidelity Is Not Hard-Coded by Purpose

DPFI MUST NOT apply a universal mapping such as:

```text
model_training -> high
testing -> medium
sandbox -> low
```

Fidelity requirements SHOULD be resolved from the applicable combination of:

```text
purpose
quality requirements
evaluation criteria
privacy requirements
risk / control requirements
cost / performance constraints
approved enterprise or HDIP Profile defaults
```

Where applicable, SYNCTX SHOULD reference the resolved fidelity concept through:

```text
synctx:hasFidelityLevelRef
```

### Rule 4.3 — Preserve Only Declared/Required Characteristics

DPFI MUST NOT universally require preservation of statistical distribution or any other characteristic.

The generation contract/context MAY require preservation or controlled transformation of characteristics such as:

```text
referential integrity
statistical distributions
temporal relationships
semantic constraints
population ratios
rare-event characteristics
causal or scenario constraints
```

Synthetic generation MAY intentionally alter distributions for legitimate purposes such as augmentation, balancing, simulation, stress testing, privacy protection or bias correction.

### Phase 4 Result

```text
GenerationRequirements = ResolveGenerationRequirements(
    Purpose,
    RelationshipBindings,
    BA,
    UC,
    QualityRequirements,
    EvaluationCriteria,
    ApplicableProfiles
)
```

---

## 🔹 Phase 5 — Constraint Projection Compilation

### Objective

Project applicable authoritative obligations into SYNCTX without creating a second policy vocabulary or pretending that every policy is machine-executable.

### Rule 5.1 — Resolve Applicable Constraints

DPFI MUST resolve applicable obligations from sources such as:

```text
Policy Intent
enterprise/domain policy
Data Contracts
Business Assertions
privacy obligations
quality requirements
regulatory obligations
approved generation requirements
```

### Rule 5.2 — Compile Constraint Projections, Not New Policy Authority

For each applicable obligation, DPFI MAY create:

```text
synctx:ConstraintProjection
```

that references the authoritative source using:

```text
synctx:constraintRef
```

and, where governed, an applicable controlled constraint kind using:

```text
synctx:constraintKindRef
```

The projection MUST NOT become the authority for the underlying policy or rule.

### Rule 5.3 — Machine-Executable and Assessment-Required Obligations Stay Distinct

Where an obligation can be deterministically compiled, DPFI MAY produce an executable control requirement or typed value in the projection.

Where the obligation requires judgement or external assessment, DPFI MUST preserve that fact rather than pretending it has been machine-resolved.

### Rule 5.4 — No Universal Privacy Transformation

A constraint such as `no_pii` MUST NOT automatically compile to one universal transformation such as `remove_pii = TRUE`.

The applicable transformation may instead require one or more governed controls such as:

```text
exclude
generalise
mask
tokenise
replace
aggregate
regenerate
restrict
```

The selected control must remain traceable to the authoritative obligation and approved realization.

### Rule 5.5 — Regulatory Constraints Must Preserve Source and Scope

Where residency, retention, disclosure, masking or similar regulatory obligations apply, the resulting ConstraintProjection MUST preserve sufficient reference/context to identify the governing source and applicable scope.

### Phase 5 Result

```text
ConstraintProjections = CompileApplicableConstraints(
    PI,
    Policies,
    Contracts,
    BA,
    RegulatoryObligations,
    GenerationRequirements
)
```

---

## 🔹 Phase 6 — SYNCTX Assembly & Versioning

### Objective

Assemble the validated SYNCTX projection. This phase does **not** execute synthetic generation and does **not** create Product identity.

### Rule 6.1 — Assemble Canonical SYNCTX Projection

DPFI MUST assemble the applicable resolved state using the canonical SYNCTX ontology:

```text
SyntheticContext
  +--> hasMemberVersion
  +--> hasPurpose
  +--> hasRelationshipBinding
  +--> hasConstraintProjection
  +--> generationModeRef        where applicable
  +--> hasFidelityLevelRef      where applicable
  +--> requestedBy              where known
  +--> requestedFor             where known
  +--> appliedBy
  +--> createdOn
  +--> versionIdentifier
  +--> statusRef                where applicable
```

### Rule 6.2 — SYNCTX Does Not Create Synthetic Products

DPFI MUST NOT perform logic equivalent to:

```text
FOR each member:
    CREATE synthetic_product
```

The correct boundary is:

```text
SYNCTX
   |
   v
synthetic-generation activity / execution
   |
   v
generated Data / Data Asset
   |
   | intentional Product constitution, if applicable
   v
Synthetic Data Product
```

Generated output becomes a Product only through the applicable BPS/PIN and Data Product lifecycle/qualification rules.

### Rule 6.3 — Output Cardinality Is Not Derived from Member Count

One SYNCTX may later support generation of:

```text
one generated dataset
multiple generated datasets
one consolidated dataset
scenario bundles
graph outputs
other governed generated assets
```

DPFI MUST NOT infer one output per member Product Version.

### Rule 6.4 — No Ambiguous `basedOn` Relationship

SYNCTX compilation MUST preserve distinct relationship semantics.

```text
dependency
!= provenance
!= derivation
!= membership
```

Future generated assets or Products SHOULD use the applicable authoritative dependency/provenance/derivation relations established by their governing specifications.

### Rule 6.5 — Versioned Historical Meaning

Once a SYNCTX version has been used for generation, material changes to any of the following SHOULD result in a new SYNCTX version rather than silent mutation:

```text
member Product Versions
relationship bindings
constraints
purpose
generation mode
fidelity requirements
other material generation requirements
```

Revision relationships SHOULD preserve historical meaning, for example through W3C PROV revision semantics where applicable.

### Phase 6 Result

```text
SYNCTX = AssembleVersionedProjection(
    MemberVersions,
    Purpose,
    RelationshipBindings,
    GenerationRequirements,
    ConstraintProjections,
    RequestContext,
    CompilerMetadata
)
```

---

## 🔹 Phase 7 — Validation & Publication

### Objective

Validate that the compiled context is complete enough for its declared purpose and publish/register the resulting SYNCTX version for downstream HDIP use.

### Rule 7.1 — Minimum Membership

```text
IF MemberVersions.count < 1
THEN INVALID
```

### Rule 7.2 — All Member Version References Must Resolve

Every member reference MUST identify a resolvable Product Version or the compilation MUST fail/escalate.

### Rule 7.3 — Relational Requirements Drive Relationship Validation

Multiple members do **not** automatically require record-level joinability.

```text
members.count > 1
    != relationship required
```

However:

```text
IF generation requirements require
cross-member relational preservation
AND no sufficient validated RelationshipBinding exists
THEN FAIL / INDETERMINATE
```

### Rule 7.4 — Relationship Bindings Must Be Internally Consistent

Every RelationshipBinding MUST:

```text
reference valid member endpoints
retain evidence/authority for its semantic and/or technical basis
avoid unresolved material conflict
```

### Rule 7.5 — Constraint References Must Resolve

Every material ConstraintProjection MUST preserve a resolvable authoritative source reference or be explicitly marked unresolved/assessment-required according to governance rules.

### Rule 7.6 — Purpose Must Be Known

A SYNCTX MUST have a governed purpose reference sufficient to explain why it was compiled and to assess whether its member, relationship and constraint state is applicable.

### Rule 7.7 — Generation Requirements Must Be Sufficiently Resolved

Where generation mode or fidelity is material to safe/correct generation, DPFI MUST resolve the applicable reference or stop/escalate compilation.

### Rule 7.8 — No Silent Guessing

If a material member, relationship, constraint, currentness or generation requirement remains ambiguous:

```text
Compilation outcome = INDETERMINATE / FAIL / ESCALATE
```

according to the applicable PDEP governance policy.

### Rule 7.9 — Publication Does Not Execute Generation

Publishing/registering a SYNCTX makes the compiled context available to downstream HDIP generation capabilities. It does not itself constitute a synthetic-generation execution.

### Phase 7 Result

```text
Validated SYNCTX Version
    -> registered / discoverable for approved downstream use
```

---

# 7. Formal Logical Representation

A compact representation of the reconciled process is:

```text
SyntheticApplicability =
    ResolveSyntheticApplicability(
        IR,
        PI,
        UC,
        ExplicitGenerationRequest,
        ApplicablePolicy
    )

MemberVersions =
    ResolveApplicableMemberVersions(
        PD,
        ProductVersionState,
        SyntheticApplicability
    )

RelationshipBindings =
    ResolveValidatedRelationships(
        MemberVersions,
        SD,
        EnterpriseSemantics,
        Schemas,
        DataContracts,
        BA
    )

GenerationRequirements =
    ResolveGenerationRequirements(
        UC,
        RelationshipBindings,
        BA,
        QualityRequirements,
        EvaluationCriteria,
        ApplicableProfiles
    )

ConstraintProjections =
    CompileApplicableConstraints(
        PI,
        ApplicablePolicies,
        DataContracts,
        BA,
        RegulatoryObligations,
        GenerationRequirements
    )

SYNCTX =
    AssembleAndValidate(
        MemberVersions,
        Purpose,
        RelationshipBindings,
        GenerationRequirements,
        ConstraintProjections,
        RequestContext,
        CompilerMetadata
    )
```

There is intentionally no function equivalent to:

```text
GenerateSyntheticProducts(Members)
```

inside SYNCTX compilation.

---

# 8. Canonical Graph Construction Mapping

The reconciled mapping to the SYNCTX ontology is:

```text
Member Product Versions
    -> synctx:hasMemberVersion

Validated relationship projections
    -> synctx:hasRelationshipBinding

Relationship endpoints
    -> synctx:fromVersion
    -> synctx:toVersion

Controlled relationship kind
    -> synctx:relationshipKindRef

Authoritative semantic relationship
    -> synctx:semanticRelationshipRef

Governed technical join/key binding
    -> synctx:joinBindingRef

Purpose
    -> synctx:hasPurpose

Generation mode
    -> synctx:generationModeRef

Fidelity requirement
    -> synctx:hasFidelityLevelRef

Constraint projections
    -> synctx:hasConstraintProjection

Authoritative constraint source
    -> synctx:constraintRef

Request / initiative context
    -> synctx:requestedBy
    -> synctx:requestedFor

HDIP applying capability
    -> synctx:appliedBy

Lifecycle/version
    -> synctx:createdOn
    -> synctx:versionIdentifier
    -> synctx:statusRef
```

Later generation execution may add:

```text
synthetic-generation activity
    -> synctx:usedByGeneration

generated Data / Data Asset
    -> synctx:associatedGeneratedAsset
```

These later relationships do not make SYNCTX the generator and do not confer Product status on the generated assets.

---

# 9. Determinism and Reproducibility Principle

The original goal of deterministic compilation is retained, but must be scoped precisely.

> **Given the same normalized authoritative inputs, the same member Product Versions, the same applicable semantic/policy/contract versions, and the same compiler/rule-set version, DPFI MUST produce semantically equivalent canonical SYNCTX projection content.**

Conceptually:

```text
Normalize(inputs1) = Normalize(inputs2)
AND CompilerVersion1 = CompilerVersion2
AND RuleSetVersion1 = RuleSetVersion2

=>
SemanticProjection(SYNCTX1)
    =
SemanticProjection(SYNCTX2)
```

Literal serialization details such as graph ordering, generated timestamps or non-semantic identifiers need not be byte-identical unless a later HDIP Profile explicitly requires content-addressed/canonical serialization.

Determinism of **context compilation** does not imply deterministic **synthetic-data generation**. Generation may legitimately be stochastic where governed by the applicable generation strategy.

---

# 10. Observability and Evidence

DPFI MUST produce sufficient compilation evidence to explain and reproduce the SYNCTX decision path.

At minimum, where applicable, DPFI SHOULD record:

```text
why SYNCTX compilation was required/selected
compiler version
rule-set version
normalized input versions
selected Product Versions
candidate dependencies considered
why candidate members were included/excluded
relationship evidence and authority
technical join/key evidence
constraint source and version
generation-mode decision basis
fidelity decision basis
unresolved / assessment-required obligations
validation outcome
SYNCTX identity and version produced
```

Observability records are evidence of compilation behavior; they do not independently prove semantic correctness or policy authority.

---

# 11. Explicit Non-Inference Rules

For avoidance of doubt, DPFI MUST NOT infer any of the following solely from the listed weak evidence:

```text
purpose label
    -> synthetic generation required

privacy requirement
    -> synthetic generation required

multiple dependencies
    -> SYNCTX required

transitive dependency
    -> direct SYNCTX membership

ontology relationship
    -> executable join

matching attribute names
    -> foreign key

relationship exists
    -> referential-integrity preservation required

relationship count
    -> coordinated generation

purpose label
    -> universal fidelity level

coordinated generation
    -> statistical distribution must be preserved

policy exists
    -> fully machine-executable constraint

SYNCTX member
    -> one synthetic output

generated output
    -> Product

SYNCTX
    -> GEAIRM AI Context
```

---

# 12. Relationship to PDEP and Downstream Generation

SYNCTX is generated during the PDEP compilation path where applicable.

```text
PDEP Stages 1-7
    -> declare / resolve Product intent and obligations

PDEP Stage 8
    -> DPFI resolves and compiles SYNCTX where applicable

PDEP Stage 9+
    -> approved generation/deployment capabilities may use the
       registered SYNCTX version

Synthetic-generation execution
    -> may produce generated Data / Data Assets

PDEP / BPS qualification
    -> may intentionally constitute applicable outputs as Products
```

Therefore:

```text
SYNCTX compilation
    precedes / supports generation

SYNCTX compilation
    does not itself execute generation

SYNCTX compilation
    does not itself create a Data Product
```

---

# 13. Final Principle

> **DPFI resolves and compiles governed synthetic-generation context; it does not invent semantics, authority, joinability, privacy strategy, or Product identity.**

This keeps SYNCTX useful as a platform-generated, reproducible relational and constraint projection while preserving the semantic and architectural authorities on which HDIP depends.
