#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import sys
    import os
    # sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'shared'))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "brand_and_model_service.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
