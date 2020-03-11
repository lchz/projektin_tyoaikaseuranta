# User stories

#### 1.Tiedon selaaminen

As a user, I can list all projects so that I can register for one of them.

```sql
SELECT * FROM project;
```

As a user, I can list all tasks so that I can trace my working hours.

```sql
SELECT * FROM task;
```

#### 2. Tiedon lisääminen

As a user, I can create a project so that others can register for it.

```sql
INSERT INTO project (date_created, date_modified, name, description) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, <String>, <String>);
```

As a user, I can create a task to record my working hours.

```sql
INSERT INTO task (date_created, date_modified, name, content, estimatedTime, date, status) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, <String>, <String>, <Numeric>, <Date>, <Boolean>);
```

As a user, I can register for a project.

```sql
INSERT INTO registration_table (project_id, account_id) VALUES (<Integer>, <Integer>);
```

#### 3. Tiedon muokkaaminen

As a user, I can set my actual hours spent on the task.

```sql
UPDATE task SET actualTime=<Numeric> WHERE id=<task_id>;
```

As a user, I can set status of a task as done when I finished it.

```sql
UPDATE task SET status=True WHERE id=<task_id>;
```

#### 4. Tiedon poistaminen

As a user, I can remove a task created by myself.

```sql
DELETE FROM task WHERE id=<task_id>;
```
