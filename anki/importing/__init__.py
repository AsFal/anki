# -*- coding: utf-8 -*-
# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

from anki.importing.csvfile import TextImporter
from anki.importing.anki2 import Anki2Importer
from anki.importing.anki1 import Anki1Importer
from anki.importing.supermemo_xml import SupermemoXmlImporter
from anki.lang import _

Importers = (
    (_("Text separated by tabs or semicolons (*.txt,*.csv)"), TextImporter),
    (_("Anki 2.0 Deck (*.anki2)"), Anki2Importer),
    (_("Anki 1.2 Deck (*.anki)"), Anki1Importer),
    (_("Supermemo XML export (*.xml)"), SupermemoXmlImporter),
    )
