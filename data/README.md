This dataset contains metadata for 279 video clips. Each video clip belongs to exactly one of the following categories:

* Cats (55 videos)
* Magic (47 videos)
* Funny Gaming Clips (177 videos)

Each video object has the following properties:

* `relevant_topics` (list of strings that are freebase topic ids, assigned by YouTube)
* `topics` (list of strings that are freebase topic ids, assigned by YouTube)
* `title` (string, assigned by the video uploader)
* `target_category_id` (integer, refers to category id as in categories.json)
* `tags` (list of strings, assigned by the video uploader)

The list of videos is shuffled
