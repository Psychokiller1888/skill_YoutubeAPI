from core.base.model.AliceSkill import AliceSkill
from core.dialog.model.DialogSession import DialogSession
from core.util.Decorators import IntentHandler


class YoutubeAPI(AliceSkill):
	"""
	Author: Psychokiller1888
	Description: Access and manage your youtube account
	"""

	@IntentHandler('MyIntentName')
	def dummyIntent(self, session: DialogSession, **_kwargs):
		pass
