# Contributing to kontakt2mpce

Thank you for your interest in contributing to kontakt2mpce! This document provides guidelines for contributing to the project.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/AdamJablonski/kontakt2mpce.git
   cd kontakt2mpce
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   # or
   pip install -r requirements.txt
   ```

4. Install FFmpeg (required for audio conversion):
   - **macOS:** `brew install ffmpeg`
   - **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
   - **Windows:** Download from https://ffmpeg.org/

## Project Structure

```
kontakt2mpce/
├── src/
│   └── kontakt2mpce/
│       ├── __init__.py
│       ├── cli.py           # Command-line interface
│       ├── converter.py     # Main conversion logic
│       ├── parsers/         # NKI format parsers (planned)
│       ├── generators/      # XPM format generators (planned)
│       └── audio/           # Audio conversion utilities (planned)
├── tests/
│   └── test_basic.py
├── PLAN.md                  # Detailed project plan
├── README.md
├── pyproject.toml
└── requirements.txt
```

## Development Workflow

1. **Create a branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the coding standards below

3. **Run tests**:
   ```bash
   pytest
   ```

4. **Format your code**:
   ```bash
   black src/ tests/
   ```

5. **Lint your code**:
   ```bash
   flake8 src/ tests/
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

7. **Push and create a pull request**:
   ```bash
   git push origin feature/your-feature-name
   ```

## Coding Standards

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use [Black](https://black.readthedocs.io/) for code formatting (line length: 100)
- Write docstrings for all functions, classes, and modules
- Add type hints where appropriate
- Write tests for new functionality

## Testing

- Write unit tests for all new functions
- Aim for high test coverage (>80%)
- Test with real Kontakt instruments when possible
- Include edge cases and error handling

## Areas Needing Help

### High Priority
1. **Kontakt Format Research**
   - Reverse engineering Kontakt 5-8 binary format
   - Documenting zone/group data structures
   - Testing with various Kontakt versions

2. **Core Implementation**
   - NKI parser implementation
   - XPM generator implementation
   - Audio format conversion utilities

### Medium Priority
3. **Testing**
   - Creating test fixtures (sample NKI files)
   - Testing with real-world Kontakt libraries
   - Validation with MPC hardware/software

4. **Documentation**
   - Usage examples and tutorials
   - Video demonstrations
   - Format specifications

### Future Enhancements
5. **Advanced Features**
   - GUI application
   - Batch conversion mode
   - More parameter mapping
   - SFZ support

## Reporting Issues

When reporting bugs, please include:
- Kontakt version and instrument details
- Error message and stack trace
- Steps to reproduce
- Expected vs. actual behavior

## Questions?

Feel free to open an issue for questions or discussion.

## Code of Conduct

Be respectful and constructive in all interactions. We aim to create a welcoming environment for all contributors.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
