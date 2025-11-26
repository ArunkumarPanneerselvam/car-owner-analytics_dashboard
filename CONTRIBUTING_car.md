# Contributing to Car Owner Analytics Dashboard

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

Before submitting a bug report:
- Check existing issues to avoid duplicates
- Test with the latest version
- Gather relevant information (Python version, OS, error messages)

Create a detailed bug report including:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Screenshots or error messages
- Environment details (Python version, OS, browser)

### Suggesting Features

Feature requests are welcome! Include:
- Clear description of the feature
- Use cases and benefits
- Potential implementation approach
- Examples from other projects (if applicable)

### Pull Requests

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes:
   - Write clear, commented code
   - Follow PEP 8 style guidelines
   - Add docstrings to functions
   - Update documentation as needed

4. Test your changes:
   - Run the data generator
   - Test dashboard functionality
   - Check all filters work correctly
   - Verify visualizations display properly

5. Commit with clear messages:
   ```bash
   git commit -m "Add: brief description of changes"
   ```

6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

7. Open a Pull Request with:
   - Clear title and description
   - Link to related issues
   - Screenshots (if UI changes)
   - Test results

## Code Standards

### Python Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Maximum line length: 100 characters
- Use type hints where appropriate

### Code Organization
- Keep functions focused and concise
- Add docstrings to all functions
- Group related functionality
- Use constants for magic numbers

### Example Function Structure
```python
def filter_data(df: pd.DataFrame, filters: dict) -> pd.DataFrame:
    """
    Filter dataframe based on provided criteria.

    Args:
        df: Input dataframe
        filters: Dictionary of filter criteria

    Returns:
        Filtered dataframe
    """
    # Implementation
    return filtered_df
```

## Testing

Before submitting:
- Test data generation with different parameters
- Verify all dashboard filters work
- Test with different data sizes
- Check browser console for errors
- Test on multiple browsers (Chrome, Firefox, Safari)

## Documentation

Update documentation for:
- New features or filters
- Changed functionality
- New dependencies
- Configuration options

## Questions?

Feel free to:
- Open an issue for discussion
- Ask questions in pull requests
- Contact maintainers directly

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

Thank you for contributing! 🎉
