#!/usr/bin/env python3
# -*- coding: uft-8 -*-
#单元测试

class Dict(dict):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        
    def __getattr__(self, key):
        try:
            return self[key]
        except :
            raise AttributeError(r"'Dict' has no '%s'" % key)
            
    def __setattr__(self, key, value):
        self[key] = value
        
d = Dict(a = 1, b = 2)
print(d)

import unittest

#第二个py文件
#from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
if __name__ == '__main__':
    unittest.main()