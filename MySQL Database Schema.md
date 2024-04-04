# MySQL Database Schema

This file outlines the schema of a MySQL database, detailing all tables, columns, and their relationships. The relationships are depicted using symbols to represent the type and direction of connections between tables, based on foreign keys.

### Relationship Symbols:
- `<<-->>`: Many-to-Many Relationship. Multiple records in one table are associated with multiple records in another, typically via a junction table.
- `<<-->`: One-to-Many Relationship (One on the right). A single record in the right table can be associated with multiple records in the left table.
- `<-->>`: One-to-Many Relationship (One on the left). A single record in the left table can be associated with multiple records in the right table.
- `<-->`: One-to-One Relationship. A record in one table is associated with only one record in another table.

### Primary Key Indication:
- `#` : If a column name starts with a `#` it means that it is the primary key of the table.

## MySQL Table Schema for Database: superadmin_pioneer

<details>
<summary>acl_rules</summary>

  - #id
  - user_id <<--> users.id (FK: acl_rules_user_id_foreign)
  - disk
  - path
  - access
  - created_at
  - updated_at

</details>

<details>
<summary>acl_rules_roles</summary>

  - #id
  - role_id <<--> roles.id (FK: acl_rules_role_role_id_foreign)
  - disk
  - path
  - access
  - created_at
  - updated_at

</details>

<details>
<summary>categories</summary>

  - #id
  - name
  - slug
  - created_at
  - updated_at

</details>

<details>
<summary>contents</summary>

  - #id
  - title
  - featured_image
  - intro_text
  - full_text
  - created_at
  - updated_at
  - categories_id <<--> categories.id (FK: contents_ibfk_1)
  - recipient

</details>

<details>
<summary>delivery</summary>

  - #id
  - message_id
  - sent_time
  - delivered
  - seen
  - seen_time
  - created_at
  - updated_at

</details>

<details>
<summary>failed_jobs</summary>

  - #id
  - uuid
  - connection
  - queue
  - payload
  - exception
  - failed_at

</details>

<details>
<summary>farmers</summary>

  - #id
  - name
  - surname
  - email
  - number
  - location
  - lat
  - lng
  - field
  - created_at
  - updated_at
  - username
  - password
  - auto
  - active
  - login_date
  - profile_pic
  - user_note
  - dob
  - notify
  - remember_token
  - categories

</details>

<details>
<summary>farmers2</summary>

  - id
  - name
  - surname
  - email
  - number
  - location
  - lat
  - lng
  - field
  - created_at
  - updated_at
  - username
  - password
  - auto
  - active
  - login_date
  - profile_pic
  - user_note
  - dob
  - notify
  - remember_token
  - categories

</details>

<details>
<summary>farmers_copy1</summary>

  - #id
  - name
  - surname
  - email
  - number
  - location
  - lat
  - lng
  - field
  - created_at
  - updated_at
  - username
  - password
  - auto
  - active
  - login_date
  - profile_pic
  - user_note
  - dob
  - notify
  - remember_token
  - categories

</details>

<details>
<summary>farmer_categories</summary>

  - #id
  - name
  - visible
  - created_at
  - updated_at

</details>

<details>
<summary>file_access_logs</summary>

  - #id
  - doc_path
  - filename
  - access_type
  - user_id
  - created_at
  - updated_at
  - recipient

</details>

<details>
<summary>file_manager_links</summary>

  - #id
  - path
  - name
  - link
  - created_at
  - updated_at

</details>

<details>
<summary>file_permissions</summary>

  - #id
  - category_id <<--> farmer_categories.id (FK: file_permissions_ibfk_1)
  - full_path
  - created_at
  - updated_at

</details>

<details>
<summary>login_logs</summary>

  - #id
  - user_id
  - created_at
  - updated_at

</details>

<details>
<summary>medias</summary>

  - #id
  - name
  - created_at
  - updated_at
  - slug
  - marketing_content
  - recipient

</details>

<details>
<summary>media_links</summary>

  - #id
  - media_id <<--> medias.id (FK: media_links_ibfk_1)
  - link
  - file
  - name
  - updated_at
  - created_at
  - recipient

</details>

<details>
<summary>messages</summary>

  - #id
  - user_id
  - name
  - headline
  - content
  - created_at
  - updated_at
  - scheduled_at
  - type
  - views
  - recipient
  - meta_data

</details>

<details>
<summary>messages_copy1</summary>

  - #id
  - user_id
  - name
  - headline
  - content
  - created_at
  - updated_at
  - scheduled_at
  - type
  - views
  - recipient
  - meta_data

</details>

<details>
<summary>migrations</summary>

  - #id
  - migration
  - batch

</details>

<details>
<summary>model_has_permissions</summary>

  - #permission_id <<--> permissions.id (FK: model_has_permissions_permission_id_foreign)
  - #model_type
  - #model_id

</details>

<details>
<summary>model_has_roles</summary>

  - #role_id <<--> roles.id (FK: model_has_roles_role_id_foreign)
  - #model_type
  - #model_id

</details>

<details>
<summary>notification_bindings</summary>

  - sid
  - type
  - device_id
  - #identity
  - created_at
  - updated_at

</details>

<details>
<summary>page_access_logs</summary>

  - #id
  - page_link
  - page_slug
  - created_at
  - updated_at
  - recipient
  - user_id

</details>

<details>
<summary>password_resets</summary>

  - email
  - token
  - created_at

</details>

<details>
<summary>permissions</summary>

  - #id
  - name
  - guard_name
  - created_at
  - updated_at

</details>

<details>
<summary>roles</summary>

  - #id
  - name
  - guard_name
  - created_at
  - updated_at

</details>

<details>
<summary>role_has_permissions</summary>

  - #permission_id <<--> permissions.id (FK: role_has_permissions_permission_id_foreign)
  - #role_id <<--> roles.id (FK: role_has_permissions_role_id_foreign)

</details>

<details>
<summary>schedule</summary>

  - #id
  - message_id
  - send_time
  - created_at
  - updated_at

</details>

<details>
<summary>search_tags</summary>

  - #id
  - filename
  - tags
  - updated_at
  - created_at
  - display_name

</details>

<details>
<summary>users</summary>

  - #id
  - name
  - email
  - email_verified_at
  - password
  - remember_token
  - profile_pic
  - notes
  - created_at
  - updated_at
  - surname
  - phone_number
  - company_name
  - login_date

</details>

 - Total Unique Foreign Keys: 9