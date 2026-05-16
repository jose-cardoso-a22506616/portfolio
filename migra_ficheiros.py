import os

from django.conf import settings
from django.core.files import File

from portfolio.models import Tecnologia   # adaptar ao modelo


for obj in Tecnologia.objects.all():

    if obj.logo and obj.logo.name:

        # caminho físico do ficheiro em media/
        local_path = os.path.join(settings.MEDIA_ROOT, obj.logo.name)

        if os.path.exists(local_path):

            with open(local_path, 'rb') as f:

                obj.logo.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )

            print(f"Migrado: {obj}")

        else:
            print(f"Ficheiro não encontrado: {local_path}")