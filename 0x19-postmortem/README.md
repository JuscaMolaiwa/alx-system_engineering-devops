# Postmortem Report

![Flogging a dead horse](post-mortem-meetings.jpg)

## Issue Overview

- Shortly after launching a new feature on our Ruby on Rails website, we were inundated with complaints from users who were unable to sign in or register. Within 5 minutes of the update going live, we received 127 emails detailing login issues, which was alarming as the feature had passed testing and had worked previously. Recognizing the risk of losing these users, we quickly investigated. Re-cloning the repository and following the setup instructions revealed that the website wouldn't even start. We quickly identified that the problem stemmed from not updating the necessary project dependencies. The site remained unusable from 9:55 AM GMT+1 until 11:20 AM GMT+1.

## Incident Timeline

 - 05-02-2022 9:55 AM GMT+1: The first user reported login issues.
- 05-02-2022 10:20 AM GMT+1: Jusca, one of our backend engineers, encountered the same issue when attempting to log in.
- 05-02-2022 10:35 AM GMT+1: We began inspecting the controllers and views for potential bugs.
- 05-02-2022 10:40 AM GMT+1: We suspected the bcrypt gem (used for password hashing) was either faulty or misconfigured, as errors indicated bcrypt was failing to process valid password hashes.
- 05-02-2022 10:42 AM GMT+1: We explored the possibility of form fields being incorrectly mapped to models, but this was ruled out.
- 05-02-2022 10:45 AM GMT+1: There was concern that the controllers were generating an incorrect hash for valid admin passwords.
- 05-02-2022 10:50 AM GMT+1: Jusca hypothesized that the password wasn't being hashed correctly.
- 05-02-2022 11:00 AM GMT+1: The backend team was officially involved to resolve the issue.
- 05-02-2022 11:20 AM GMT+1: The problem was resolved after manually updating the bcrypt gem in the Gemfile.lock to a compatible version and reinstalling dependencies.
﻿


## Root Cause and Solution

- The issue stemmed from the outdated version of the bcrypt gem, which failed to handle password hashes properly. The version we had installed was incompatible with the hashing mechanism in our app. Jusca corrected this by updating the Gemfile.lock to include a newer version of bcrypt, and once the necessary gems were reinstalled, the site functioned correctly.

## Preventative Actions

- Implement continuous integration (CI) to trigger builds on each pull request, ensuring the branch passes all tests before merging.
Set up monitoring tools to track both the application server and the database, helping us detect future problems earlier.
Require all new features to pass a set of predefined tests before they can be merged into the deployment branch.
