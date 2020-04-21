# User stories

## 1.Tiedon selaaminen

As a user, I can log in to the system so that I can se project details.
```sql
SELECT * FROM account WHERE username=<String> AND password=<String>
```

As a user, I can list all projects so that I can check the details of them.
```sql
SELECT * FROM project;
```

As a user, I can list all tasks so that I can trace my working hours.
```sql
SELECT * FROM Task;
```

As a user, I can see details of a project so that I can ???.
```sql
SELECT <project> FROM Project WHERE project.id=<id>;
```

As a master, I can see registered participants in the project.
```sql
SELECT Account.id, Account.name FROM Registration
    LEFT JOIN Account ON Registration.account_id = Account.id
    WHERE Registration.project_id = :project_id
```

As a master, I can see how many tasks in total, how many completed tasks and how many uncompleted tasks have been registered per participant.
```sql
SELECT COUNT(Task.id) from Task
    LEFT JOIN Project ON Project.id = Task.project_id
    LEFT JOIN Account ON Account.id = Task.account_id
    WHERE Project.id = <project_id>
    AND Account.id = <account_id>

SELECT COUNT(Task.id) from Task
    LEFT JOIN Project ON Project.id = Task.project_id
    LEFT JOIN Account ON Account.id = Task.account_id
    WHERE Project.id = <project_id>
    AND Account.id = <account_id>
    AND Task.status = True

SELECT COUNT(Task.id) from Task
    LEFT JOIN Project ON Project.id = Task.project_id
    LEFT JOIN Account ON Account.id = Task.account_id
    WHERE Project.id = <project_id>
    AND Account.id = <account_id>
    AND Task.status = False
```

As a master, I can see how many hours in total have been used in the project.
```sql
SELECT SUM(Task.\"estimatedTime\"), SUM(Task.\"actualTime\") FROM Task
    LEFT JOIN Project ON Project.id = Task.project_id
    WHERE Project.id = <project_id>
```

As a master, I can see how many hours in total have been used in the project per participant.

As a basic user, I can see how many hours in total I have been used in the project.
```sql
SELECT SUM(Task.\"estimatedTime\"), SUM(Task.\"actualTime\") FROM Task
    LEFT JOIN Account ON Account.id = Task.account_id
    LEFT JOIN Project ON Project.id = Task.project_id
    WHERE Account.id = <account_id>
    AND Project.id = <project_id>
```

As a master, I can search for the working time report for one week so that I can know how much time in total has been used in the week.
```sql
SELECT SUM(Task.\"estimatedTime\"), SUM(Task.\"actualTime\") FROM Task
    LEFT JOIN Project ON project.id = Task.project_id
    WHERE project.id = <project_id>
    AND Task.date_modified >= <fromDate>
    AND Task.date_modified <= <toDate>
```

As a basic user, I can search for the working time report for one week so that I can know how much time in total I have been used in the week.
```sql
SELECT SUM(Task.\"estimatedTime\"), SUM(Task.\"actualTime\") FROM Task
    LEFT JOIN Project ON project.id = Task.project_id
    WHERE project.id = <project_id>
    AND Task.account_id = <account_id>
    AND Task.date_modified >= <fromDate>
    AND Task.date_modified <= <toDate>
```

As a basic user, I can find the tasks registered by myself.
```sql
SELECT Task.name, Task.status, Task.date_created, Task.date, Task.id FROM Task
    LEFT JOIN Project ON Project.id = Task.project_id
    WHERE Task.account_id = :current_id
    AND Task.project_id = :project_id
```



## 2. Tiedon lisääminen

As a user, I can create a new account so that I can use more functionalities
```sql
INSERT INTO account (date_created, date_modified, name, username, password VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, <String>, <String>, <String>)
```

As a master, I can create a project so that others can register for it.

```sql
INSERT INTO project (date_created, date_modified, name, description) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, <String>, <String>);
```

As a basic user, I can create a task to record my working hours.

```sql
INSERT INTO task (date_created, date_modified, name, content, estimatedTime, date, status) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, <String>, <String>, <Numeric>, <Date>, <Boolean>);
```

As a basic user, I can register for a project so that I can start to trace my working hours on the project.

```sql
INSERT INTO registration_table (project_id, account_id) VALUES (<Integer>, <Integer>);
```



## 3. Tiedon muokkaaminen

As a user, I can set my actual hours spent on the task when the task is completed so that the system will record my working time.

```sql
UPDATE task SET actualTime=<Numeric> WHERE task.id=<task_id>;
UPDATE task SET status=True WHERE task.id=<task_id>;
```



## 4. Tiedon poistaminen

As a basic user, I can remove a task created by myself.

```sql
DELETE FROM task WHERE task.id=<task_id>;
```

As a master, I can remove a participant from the project.
```sql
DELETE FROM registration 
    WHERE project_id=<project_id> 
    AND account_id=<account_id>

DELETE FROM Task 
    WHERE Task.project_id = :project_id 
    AND Task.account_id = :account_id
```



## CREATE TABLE-lauseet

```sql
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username)
);

CREATE TABLE role (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(50), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);

CREATE TABLE project (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	description VARCHAR(1000) NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE user_role (
	role_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (role_id, account_id), 
	FOREIGN KEY(role_id) REFERENCES role (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

CREATE TABLE task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	content VARCHAR(350) NOT NULL, 
	"estimatedTime" NUMERIC(10, 1) NOT NULL, 
	"actualTime" NUMERIC(10, 1) NOT NULL, 
	date DATE NOT NULL, 
	status BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	project_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (status IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(project_id) REFERENCES project (id)
);

CREATE TABLE registration (
	project_id INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (project_id, account_id), 
	FOREIGN KEY(project_id) REFERENCES project (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
);

```