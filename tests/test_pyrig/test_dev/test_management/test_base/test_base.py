"""Tests module."""

from pyrig.dev.management.package_manager import PackageManager


class TestTool:
    """Test class."""

    def test_L(self) -> None:  # noqa: N802
        """Test method."""
        assert PackageManager.L is PackageManager

    def test_name(self) -> None:
        """Test method."""
        # Tool is abstract, test through concrete implementation
        assert PackageManager.name() == "uv"

    def test_get_args(self) -> None:
        """Test method."""
        # Tool is abstract, test through concrete implementation
        result = PackageManager.get_args("run", "pytest")
        assert result == ("uv", "run", "pytest")
