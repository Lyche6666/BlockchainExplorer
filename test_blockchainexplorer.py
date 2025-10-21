# test_blockchainexplorer.py
"""
Tests for BlockchainExplorer module.
"""

import unittest
from blockchainexplorer import BlockchainExplorer

class TestBlockchainExplorer(unittest.TestCase):
    """Test cases for BlockchainExplorer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainExplorer()
        self.assertIsInstance(instance, BlockchainExplorer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainExplorer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
