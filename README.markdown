Pingbullet regularly pings you via Pushbullet


1. Get your Pushbullet access token from your [Account Settings page](https://www.pushbullet.com/#settings/account).
2. [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
3. Set up the scheduler: Click "Manage App", then "Heroku Scheduler" and "Add a new job" to run `python pingbullet.py` daily, hourly or every 10 minutes.
4. Wait...
5. Ping!


For more fine-grained ping intervals, just schedule additional jobs. For example, to get a ping every 5-minutes, schedule two jobs running every 10 minutes at, say, :03 and :08. Unfortunately Heroku doesn't let you set the exact start time, so you may need to repeatedly add and remove jobs to get the spacing you're looking for. On the upside, [Heroku's billing is prorated to the second](https://devcenter.heroku.com/articles/usage-and-billing#computing-usage), so even with additional jobs, you're still likely to fall within their free tier.
