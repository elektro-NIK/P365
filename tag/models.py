import tagulous.models


class TagModel(tagulous.models.TagModel):
    class TagMeta:
        force_lowercase = True
        autocomplete_view = 'tag_autocomplete'
