# pwd-gen

Yet another password generator.

## Setup

Install the dependencies.

```bash
make init
```

## Usage

Use tab completion to see available commands and options.

Generate a password.

```bash
pwd-gen pwd
```

Generate an RSA key pair.

```bash
pwd-gen rsa
```

## Production

Build the CLI.

```bash
make build
```

## Miscellaneous

### Format / Lint

Format the codebase.

```bash
make write
```

Lint the codebase.

```bash
make check
```

### Cleanup

Clean up the codebase.

```bash
make clean
```
