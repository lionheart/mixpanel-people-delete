#!/usr/bin/env python

from mixpanel_api import Mixpanel
import os

num_projects = int(os.environ.get("NUM_PROJECTS", 0))

for i in range(num_projects):
    MIXPANEL_SECRET = os.environ.get("MIXPANEL_SECRET_" + str(i))
    MIXPANEL_TOKEN = os.environ.get("MIXPANEL_TOKEN_" + str(i))

    mixpanel = Mixpanel(MIXPANEL_SECRET, token=MIXPANEL_TOKEN)

    # mixpanel.export_people("pushpin_people_export.txt", "", timezone_offset=-8)
    mixpanel.people_delete(query_params={})
