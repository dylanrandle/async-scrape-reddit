# async-scrape-reddit
This repo is to demonstrate simple usage of python's asyncio module. Here I use it to asynchronously scrape the top posts from some interesting subreddits.

Run `python3 scrape.py` and command-click (in iTerm, at least) the links to view! Enjoy! 

Example stdout:
```
Top post for /r/nutrition: https://www.reddit.com/r/nutrition/comments/771cwb/its_hard_to_eat_really_well_when_i_go_to_my/
Top post for /r/ubuntu: https://www.reddit.com/r/Ubuntu/comments/76uq2y/wpa_vulnerability_what_wpa_vulnerability/
Top post for /r/stocks: https://www.reddit.com/r/stocks/comments/7719zr/my_thoughts_on_trxc_as_a_medical_scientist/
Top post for /r/AskScience: https://www.reddit.com/r/askscience/comments/76w48s/how_much_of_sleep_is_actual_maintenance_downtime/
Top post for /r/engineering: https://www.reddit.com/r/engineering/comments/770pt3/what_kind_of_steel_is_used_in_rollercoasters_and/
Top post for /r/climbing: https://www.reddit.com/r/climbing/comments/770kgz/climbing_carabiner_miniature_made_by_me_it_is/
Top post for /r/python: https://www.reddit.com/r/Python/comments/76yxk8/i_uploaded_to_github_hex_calendars_for_python/
Top post for /r/history: https://www.reddit.com/r/history/comments/76z06j/why_the_trial_by_ordeal_was_actually_an_effective/
Top post for /r/nhl: https://www.reddit.com/r/nhl/comments/772rkf/first_penalty_shot_at_little_caesars_arena_justin/
Top post for /r/math: https://www.reddit.com/r/math/comments/76yeoh/538_the_supreme_court_is_allergic_to_math/
Top post for /r/Space: https://www.reddit.com/r/space/comments/7713e8/astronaut_scott_kelly_i_thought_elon_musk_was/
Top post for /r/machinelearning: https://www.reddit.com/r/MachineLearning/comments/770wk1/r_portrait_mode_on_the_pixel_2_and_pixel_2_xl/
Top post for /r/learnpython: https://www.reddit.com/r/learnpython/comments/76zv1w/how_to_progress_from_intermediate_to_advanced/
Top post for /r/cpp: https://www.reddit.com/r/cpp/comments/76yzwj/restinio_03_headeronly_c14_library_that_gives_you/
Top post for /r/learnprogramming: https://www.reddit.com/r/learnprogramming/comments/76y9we/finally_started_college_for_cs_after_putting_it/
Top post for /r/food: https://www.reddit.com/r/food/comments/76z888/homemade_spicy_pork_belly_ramen_soup/
Top post for /r/Science: https://www.reddit.com/r/science/comments/76y7z6/science_ama_we_are_the_first_people_to_observe/
Top post for /r/javascript: https://www.reddit.com/r/javascript/comments/76znvm/the_math_behind_svg_path_only_gooey_effect/
Top post for /r/howtohack: https://www.reddit.com/r/HowToHack/comments/770byp/krack_what_it_is_and_how_it_works/
Top post for /r/lifehacks: https://www.reddit.com/r/lifehacks/comments/76x8cy/an_easy_way_to_organize_your_cables_and_prevent/
Top post for /r/everythingscience: https://www.reddit.com/r/EverythingScience/comments/771b75/physically_active_white_men_at_high_risk_for/
Top post for /r/compsci: https://www.reddit.com/r/compsci/comments/76yeo7/boolr_a_digital_logic_simulator/
Top post for /r/ZenHabits: https://www.reddit.com/r/ZenHabits/comments/76xjqm/if_you_are_distressed_by_anything_external_the/
Top post for /r/coding: https://www.reddit.com/r/coding/comments/76yb2m/top_10_java_blogs_for_programmers_of_all_levels/
```
