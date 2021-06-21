import unittest


from wtoolzexceptions import exceptions


class WToolzExceptions(unittest.TestCase):
    def test_ohoh(self):
        try:
            exceptions.ohoh(404, "yal")
        except Exception as e:
            self.assertIsInstance(e, exceptions.NotFound)
            self.assertEqual(e.message, "yal")
            self.assertEqual(e.code, "NotFound")
            self.assertEqual(e.http_status_code, 404)

    def test_exception_repr(self):
        exc = exceptions.NotFound()
        self.assertEqual(
            repr(exc),
            (
                "NotFound(http_status_code=404, http_status_name=Not Found, "
                "code=NotFound, message=The requested URL "
                "was not found on the server.)"
            ),
        )
        self.assertEqual(
            str(exc),
            (
                "NotFound(http_status_code=404, http_status_name=Not Found, "
                "code=NotFound, message=The requested URL "
                "was not found on the server.)"
            ),
        )

        exc = exceptions.NotFound("Jal jal.")
        self.assertEqual(
            repr(exc),
            (
                "NotFound(http_status_code=404, http_status_name=Not Found, "
                "code=NotFound, message=Jal jal.)"
            ),
        )

        exc = exceptions.HTTPException("An error message")
        self.assertEqual(
            repr(exc),
            (
                "HTTPException(http_status_code=???, "
                "http_status_name=Unknown Error, "
                "code=None, message=An error message)"
            ),
        )

    def test_to_dict(self):
        d = exceptions.NotFound().to_dict()

        self.assertEqual(
            d,
            {
                "error": {
                    "code": "NotFound",
                    "message": (
                        "The requested URL was " "not found on the server."
                    ),
                }
            },
        )


if __name__ == "__main__":
    unittest.main()
