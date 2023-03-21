from mock.tests.base import TestCase

from knowledge.utils import paginate, get_module


class BasicPaginateTest(TestCase):
    def test_paginate_helper(self):
        paginator, objects = paginate(range(0, 1000), 100, "xcvb")
        self.assertEquals(objects.number, 1)  # fall back to first page

        paginator, objects = paginate(range(0, 1000), 100, 154543)
        self.assertEquals(objects.number, 10)  # fall back to last page

        paginator, objects = paginate(range(0, 1000), 100, 1)

        self.assertEquals(len(objects.object_list), 100)
        self.assertEquals(paginator.count, 1000)
        self.assertEquals(paginator.num_pages, 10)

    def test_importer_basic(self):
        from django.template.defaultfilters import slugify

        sluggy = get_module("django.template.defaultfilters.slugify")

        self.assertTrue(slugify is sluggy)

    def test_importer_fail(self):
        self.assertRaises(ImportError, get_module, "django.notreal.america")
        self.assertRaises(
            ImportError, get_module, "django.template.defaultfilters.slugbug"
        )
