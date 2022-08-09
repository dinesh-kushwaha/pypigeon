CREATE TRIGGER after_insert_item
    AFTER INSERT
    ON items
    FOR EACH ROW
    EXECUTE PROCEDURE notify_new_item();