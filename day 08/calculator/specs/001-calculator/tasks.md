# Tasks: Simple Calculator

**Input**: Design documents from `/specs/001-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The spec requests explicit error handling and accuracy, so tests will be included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create `src/` directory
- [x] T002 Create `src/calculator/` directory
- [x] T003 Create `tests/` directory
- [x] T004 Create `tests/unit/` directory
- [x] T005 Create `tests/integration/` directory

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T006 Configure pytest in the project root

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Evaluate Basic Arithmetic Expression (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to input a simple arithmetic expression and receive the calculated numerical result, so I can perform quick calculations.

**Independent Test**: Can be fully tested by providing a valid arithmetic string and verifying the output matches the expected numerical result.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T007 [P] [US1] Create empty `tests/unit/test_parser.py`
- [x] T008 [P] [US1] Create empty `tests/unit/test_evaluator.py`
- [x] T009 [P] [US1] Create empty `tests/integration/test_cli.py`
- [x] T010 [US1] Write unit tests for expression parsing logic in `tests/unit/test_parser.py`
- [x] T011 [US1] Write unit tests for expression evaluation logic in `tests/unit/test_evaluator.py`
- [x] T012 [US1] Write integration tests for CLI input/output and error handling in `tests/integration/test_cli.py`

### Implementation for User Story 1

- [x] T013 [P] [US1] Create `src/calculator/parser.py`
- [x] T014 [US1] Implement tokenization and parsing logic in `src/calculator/parser.py`
- [x] T015 [P] [US1] Create `src/calculator/evaluator.py`
- [x] T016 [US1] Implement expression evaluation logic (order of operations, parentheses) in `src/calculator/evaluator.py`
- [x] T017 [US1] Implement error handling for invalid expressions and division by zero in `src/calculator/evaluator.py`
- [x] T018 [P] [US1] Create `src/cli.py`
- [x] T019 [US1] Implement CLI to take expression input, invoke calculator logic, and display results/errors in `src/cli.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T020 Code cleanup and refactoring in `src/calculator/parser.py`, `src/calculator/evaluator.py`, `src/cli.py`
- [x] T021 Ensure error messages are consistent and user-friendly in `src/cli.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Parser implementation before evaluator implementation
- Core calculator logic before CLI implementation

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, User Story 1 can start.
- Test file creation (T007, T008, T009) can run in parallel.
- Implementation file creation (T013, T015, T018) can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all empty test files for User Story 1 together:
Task: "Create empty tests/unit/test_parser.py"
Task: "Create empty tests/unit/test_evaluator.py"
Task: "Create empty tests/integration/test_cli.py"

# Launch all implementation file creations for User Story 1 together:
Task: "Create src/calculator/parser.py"
Task: "Create src/calculator/evaluator.py"
Task: "Create src/cli.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
