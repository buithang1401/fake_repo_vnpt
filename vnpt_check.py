CELERY_BEAT_SCHEDULE = {
    # 'scrape_main': {
    #     "task": "post_crawler.tasks.crawl_post",
    #     "schedule": 60.0,
    # },
    # 'crawl_repo': {
    #     "task": "post_crawler.tasks.crawl_repo",
    #     "schedule": 120.0,
    # },
    'crawl_file': {
        "task": "post_crawler.tasks.crawl_file",
        "schedule": 30.0,
    },
}