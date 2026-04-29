# Contributing Guidelines

First off, thank you for considering contributing to FlowAI!

## Code Style Guide
- **HTML**: Semantic tags, double quotes for attributes, consistent 2-space indentation.
- **CSS**: 
  - Use CSS variables defined in `:root`.
  - Avoid `!important`.
  - Group related properties (Layout, Typography, Visuals).
- **JavaScript/TypeScript**:
  - Prefer `const` over `let`.
  - Use arrow functions.
  - Strict equality (`===`).
  - Comment complex logic heavily.

## Commit Message Convention
We use [Conventional Commits](https://www.conventionalcommits.org/). This leads to more readable messages that are easy to follow when looking through the project history.

**Format:** `<type>(<scope>): <subject>`

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests

**Example:** `feat(auth): implement Google OAuth login`

## Pull Request Process
1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes (`npm test` - future phase).
5. Ensure your code lints (`npm run lint` - future phase).
6. Issue that pull request!

## Issue Templates
When creating an issue, please use the provided labels:
- `bug`: Something isn't working. Include steps to reproduce.
- `enhancement`: New feature or request.
- `documentation`: Improvements or additions to documentation.
