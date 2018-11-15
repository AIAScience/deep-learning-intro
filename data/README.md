This dataset contains metadata for 279 YouTube video clips. It is a small extraction of a
dataset created by the founders of MashTime (a failed video website startup).

Each video clip belongs to exactly one of the following categories:

* Cats (55 videos)
* Magic (47 videos)
* Funny Gaming Clips (177 videos)

Each video object has the following properties:

* `relevant_topics` (list of strings that are freebase topic ids, assigned by YouTube)
* `topics` (list of strings that are freebase topic ids, assigned by YouTube)
* `title` (string, assigned by the video uploader)
* `target_category_id` (integer, refers to category id as in categories.json, assigned by a MashTime founder)
* `tags` (list of strings, assigned by the video uploader)

The videos are listed in no particular order. In other words, they are shuffled.
