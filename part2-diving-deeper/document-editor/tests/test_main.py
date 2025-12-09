from src.main import DocumentEditor
import pytest


class TestDocumentEditor:
    def test_write(self):
        editor = DocumentEditor()
        editor.write('Some text here!')
        assert editor.content == 'Some text here!'

    def test_clear(self):
        editor = DocumentEditor()
        editor.write('Some new line of text!')
        editor.clear()
        assert editor.is_empty()

    def test_get_last_content(self):
        editor = DocumentEditor()
        editor.write('Some new line here')
        editor.clear()

        expected_last_content = 'Some new line here'
        last_content = editor.get_last_content()

        error_msg = (f'Last content is expected to be '
                     f'the content before last operation. '
                     f'Actual editor history {editor.history};'
                     f'error: {expected_last_content=} vs. '
                     f'{last_content=}')

        # assert last_content == expected_last_content, error_msg

        if last_content != expected_last_content:
            pytest.fail(error_msg)

    def test_raise_error_if_no_history(self):
        editor = DocumentEditor()
        with pytest.raises(ValueError) as excinfo:
            editor.get_last_content()

        assert str(excinfo.value).startswith(
            'No document history available:'
        )
        assert excinfo.type == ValueError

    def test_multiple_scenarios_at_once(self):
        editor = DocumentEditor()

        assert editor.is_empty()
        assert len(editor.history) == 0

        editor.clear()
        assert editor.is_empty()
        assert len(editor.history) == 1

        editor.write('Some line of text. ')
        editor.write('Next sentence here!')
        assert editor.content == 'Some line of text. Next sentence here!'
        assert not editor.is_empty()

    def test_initial_editor_is_empty(self):
        # GIVEN: initial document editor right after initialization (with no operations applied)
        editor = DocumentEditor()

        # WHEN: checking if the editor is empty
        is_editor_empty = editor.is_empty()

        # THEN: empty editor should be True, and history should also be empty
        assert is_editor_empty
        assert len(editor.history) == 0

    def test_clear_empty_editor_is_empty(self):
        # GIVEN: initial document editor right after initialization (with no operations applied)
        editor = DocumentEditor()

        # WHEN: clearing initial (empty) editor
        editor.clear()

        # THEN: editor should be empty, and the number of operations should be 1
        expected_number_of_operations = 1

        assert editor.is_empty()
        assert len(editor.history) == expected_number_of_operations

    def test_written_content_is_correct(self):
        # GIVEN: document editor
        editor = DocumentEditor()

        # WHEN: writing content to the document with multiple write operations
        editor.write('Some line of text. ')
        editor.write('Next sentence here!')

        # THEN: the content should be joined content from write operations
        assert editor.content == 'Some line of text. Next sentence here!'
        assert not editor.is_empty()
