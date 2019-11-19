# Takehome assignment

Imagine a product that is loosely based on Airtable that has the following data model.

**Users**
- id: string
- created_time: timestamp
- referred_by_user_id: string | null

**Workspaces**
- id: string,
- owner_id: string,
- created_time: timestamp

**Workspaces Collaborators**
 - id: string,
 - user_id: string,
 - workspace_id: string,
 - created_time: timestamp,
 - deleted_time: timestamp | null

**Invoices**
- id: string,
- date: date,
- type: string,
- workspace_id: string,
- total_cost_in_cents: integer,
- total_paid_in_credits_in_cents: integer

Workspaces are the main mechanism for collaboration on this platform and each workspace has a single owner and any number of workspace collaborators. Users can belong to multiple workspaces at the same time. Additionally, users can join and leave workspaces at any time (for simplicity, a user can only join or leave a workspace once). Workspace owners will never leave a workspace and do not appear in the workspace collaborators table.

There are two mechanisms for users signing up, they can either be invited by another user or they can sign up organically.

When a user signs up organically, a new workspace will be created for them and they will be added as the owner of that workspace.

When a user is invited by another user, a new workspace will not be created for them, instead they will be added as a collaborator to one of the inviting user's workspace. Additionally, their `referred_by_user_id` will point to the inviting user.

This platform has a paid and free tier, which is centered around workspaces. Each workspace that is on the paid tier will have an invoice generated every 28 days and will be billed $24 for each user in that workspace. Additionally, users will be prorated if they either join or leave in the middle of the invoice cycle.

Part of the growth strategy for this platform involves distributing credits to workspaces, which can be applied to invoices instead of cash. Workspaces start out with a certain amount of credit and more credit can be earned over time by taking different actions on the platform. This credit is not represented in these tables, but their impact can be seen on the invoice (`total_paid_in_credits_in_cents`).

There are three different types of invoices...
- initial: the first invoice for a workspace
- renewal: an invoice generated every 28 days representing the previous 28 days
- final: the last invoice for this workspace (which will occur on the same 28 day cadence)

## Questions

### Question 1:

Using this dataset, please calculate and plot recurring revenue over time.

Some workspaces may churn once they run out of credits. To account for this, exclude workspaces that have paid less than $10 (excluding credits) by the time the invoice is generated.

### Question 2:

Using the first initial invoice month as a cohort, build a cohort analysis table which shows the number of paid seats and number of paying workspaces for each cohort for every subsequent month.

### Question 3:

Given this dataset, is there any insight that you can glean regarding how this platform has been growing and what sort of growth we can expect in the future?

## Dataset

There are four .csv files included, each represents a different table in this data model. You can import them into postgres using the following queries.

```
CREATE TABLE invoices (
   id text,
   date date,
   type text,
   workspace_id text,
   total_cost_in_cents integer,
   total_paid_in_credits_in_cents integer
);

CREATE TABLE workspaces (
   id text,
   owner_id text,
   created_time timestamp
);

CREATE TABLE users (
   id text,
   created_time timestamp,
   referred_by_user_id text
);

CREATE TABLE workspace_collaborators (
   id text,
   user_id text,
   workspace_id text,
   created_time timestamp,
   deleted_time timestamp NULL
);

COPY invoices
FROM 'MY_PATH/invoices.csv' DELIMITER ',' CSV HEADER;

COPY workspaces
FROM 'MY_PATH/workspaces.csv' DELIMITER ',' CSV HEADER;

COPY users
FROM 'MY_PATH/users.csv' DELIMITER ',' CSV HEADER;

COPY workspace_collaborators
FROM 'MY_PATH/workspace_collaborators.csv' DELIMITER ',' CSV HEADER NULL AS '';
```

## Evaluation criteria

For each question, we'd like to see a short write-up describing your solution and how you arrived there. Please document any assumptions you made, the reasons why you made them, and any issues that you foresee with your approach, either now or in the long-term. If you run into an issue with an edge-case or invalid data, feel free to make a decision and document your reasoning.

You should include all the code or queries needed in your analysis and we'll be looking to make sure they are well-structured and maintainable. If you did any additional work in the process of answering these questions, please include it.

You can use any language or tools to answer this assigment, however you should choose something that would scale when the datasets do not fit in memory. For example, doing all of this analysis in Excel would not scale and therefore not be appropriate, however using Excel to generate visualizations and examine results of a SQL query would be acceptable.

Please don't spend more than 5 hours on this assignment. If you run out of time, you can include a list of next steps.
