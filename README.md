# Typescript Template

## Configuration

When `strict` is enabled, it is actually shorthand for enabling the following:

- `noImplicitAny`
- `noImplicitThis`
- `alwaysStrict`
- `strictBindCallApply`
- `strictNullChckes`
- `strictFunctionTypes`
- `strictPropertyInitialization`

## Packages

### Dev

- `typescript`: Typescript compiler.
- `@tsconfig/recommended`: Collection of recommended `tsconfig.json` files.
- `eslint`: Linter.
  - `@typescript-eslint/eslint-plugin`: Provides rules for Typescript.
  - `@typescript-eslint/parser`: Parser which allows ESLint to lint Typescript.
  - `eslint-config-prettier`: Disables formatting rules in ESLint that Prettier will be responsible for.
  - `eslint-plugin-import`: Tells ESLint how to resolve imports.
- `prettier`: Code formatter.
