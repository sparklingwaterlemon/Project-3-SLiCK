## Welcome to SLiCK

SLiCK is the newest fantasy sports web app. I allows you to pick 3 NFL teams and compare with other users who chose the teams with the highest total score. With the ability to create, update and delete bets for authorized users all the functionality they would hope for. 

#### The Interface

Opend to home page with brief description of the app.

![Home](/screenshots/home.png)

If you are a user and are not logged in you can login here.

![login](/screenshots/login)

If you are not an existing user you can create a new account here

![Sign Up](/screenshots/sign-up.png)

You will then go to a page showing your existing bets. As a new user there will be none.

![No Bets](/screenshots/no-bets.png)

You can add a name and wager to a new bet.

![Add Bet](/screenshots/add-bet.png)

Then you will be able to choose your teams.

![Add Teams](/screenshots/add-teams.png)

If teams have already played they will not be able to be chosen.

![Played Teams](/screenshots/played-teams.png)

Once you have chosen 3 teams you will no longer be able to choose anymore.

![Limit Teams](/screenshots/limit-teams.png)

As scores are updated teams will no longer be able to be removed and the total score will update.

![Team Score](/screenshots/team-score.png)

You can edit and delete your bets.

![Edit Bet](/screenshots/edit-bet.png)

![Delete Bet](/screenshots/delete-bet.png)

Once bets are created you will be able to view them here. 

![View Bets](/screenshots/view-bets.png)

If signed in as an admin you can view, create, delete and edit teams.

![Admin Abilities](/screenshots/team-index.png)

![Admin Abilities](/screenshots/edit-team.png)

![Admin Abilities](/screenshots/create-team.png)

![Admin Abilities](/screenshots/delete-team.png)

The app is responsive to smaller and larger screens using a navbar.

![Responsive](/screenshots/responsive.png)

![Navbar](/screenshots/navbar.png)







#### Technologies Used

-Django
-Python
-Html
-Materialize
-Javascript
-Heroku


#### Approach

- Created ERD, Wireframes and Terllo board to map out the app.
- Assigned roles to members of the team
    - Michael Linch: Scrum and Documenter
    - Navjeet Chatta: Git Manager
    - Vincent Slater: Design Manager
    - Michael Kim: Database Manager
- Created CRUD operations for bets
    - creating paths, urls and views for each operation
- Created users to allow there to be 1:M relationship
    - included login, log out and sign up functionality
- Created teams and there M:M relationship  with bets
- Added restrictions to non-authorized user
    - CUD ooperations for bets
- Limited the amount of teams a user could choose
- Ability to remove teams from bet
- Created function to add total bet score as scores are updated
- Added restrictions to users who are not admin
    - CUD operations for teams
- Restircted users from adding teams who have or are currently playing a game.
- Restricted users from remove teams who have or are currently playing a game.

#### What went well...



#### Hurdles



#### Ice Box

- Being able to search and compare scores with other users
- Adding other sports or players
- Adding team and user pictures
- Creating a league to play against all season
- Using an API to update teams and scores

#### [Good Luck](https://slick-betting2.herokuapp.com/)