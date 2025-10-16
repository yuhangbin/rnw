"""
Document processor using markitdown library.

This module demonstrates using the markitdown library that's defined
as a runtime dependency in pyproject.toml.
"""

from markitdown import MarkItDown
from pathlib import Path
from typing import Optional, Dict, Any
import tempfile
import os


def convert_document_to_markdown(file_path: str) -> Dict[str, Any]:
    """
    Convert various document formats to markdown using markitdown.
    
    Args:
        file_path: Path to the document file
        
    Returns:
        Dictionary containing conversion results
        
    Example:
        >>> result = convert_document_to_markdown("document.pdf")
        >>> print(result["markdown_content"])
    """
    try:
        # Initialize MarkItDown
        md = MarkItDown()
        
        # Convert the document
        result = md.convert(file_path)
        
        return {
            "success": True,
            "file_path": file_path,
            "markdown_content": result.text_content,
            "title": getattr(result, 'title', None),
            "error": None
        }
        
    except Exception as e:
        return {
            "success": False,
            "file_path": file_path,
            "markdown_content": None,
            "title": None,
            "error": str(e)
        }


def create_sample_document() -> str:
    """
    Create a sample text document for demonstration.
    
    Returns:
        Path to the created sample document
    """
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write("""# Sample Document

This is a sample document created for demonstration purposes.

## Features

- Document conversion
- Markdown output
- Error handling

## Calculator Integration

This document can be processed alongside our calculator functionality:
- Addition: 2 + 3 = 5
- Subtraction: 10 - 4 = 6
- Multiplication: 3 × 4 = 12
- Division: 15 ÷ 3 = 5

## Conclusion

The markitdown library allows us to convert various document formats
to markdown, making them easier to process and analyze.
""")
        return f.name


def demo_document_processing() -> None:
    """
    Demonstrate document processing capabilities.
    """
    print("📄 Document Processing Demo")
    print("=" * 40)
    
    # Create a sample document
    sample_file = create_sample_document()
    print(f"Created sample document: {sample_file}")
    
    try:
        # Convert the document
        result = convert_document_to_markdown(sample_file)
        
        if result["success"]:
            print("✅ Document converted successfully!")
            print("\n📝 Markdown Content:")
            print("-" * 30)
            print(result["markdown_content"])
            print("-" * 30)
        else:
            print(f"❌ Conversion failed: {result['error']}")
            
    finally:
        # Clean up the temporary file
        if os.path.exists(sample_file):
            os.unlink(sample_file)
            print(f"\n🧹 Cleaned up temporary file: {sample_file}")


if __name__ == "__main__":
    demo_document_processing()