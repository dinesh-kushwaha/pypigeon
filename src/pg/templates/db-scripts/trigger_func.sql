CREATE or REPLACE FUNCTION trigger_func()
    RETURNS trigger
     LANGUAGE 'plpgsql'
as $$
declare
begin
    if (tg_op = 'INSERT') then
        perform pg_notify('new_item_added',
        json_build_object(
             'item_no', NEW.item_no,
             'item_desc', NEW.item_description
           )::text);
    end if;
    return null;
end
$$;