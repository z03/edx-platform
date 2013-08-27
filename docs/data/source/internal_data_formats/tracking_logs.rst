#############
Tracking Logs
#############

The following is an inventory of all LMS event types. 

*************
Common Fields
*************
This section contains a table of fields common to all events.


  .. list-table::
     :widths: 10 40 10 25
     :header-rows: 1
     
     * - Common Field
       - Details
       - Type
       - Values/Format
     * - :code:`agent`
       - Browser agent string of the user who triggered the event.
       - string
       - 
     * - :code:`event`
       - Specifics of the triggered event.
       - string/JSON
       - 
     * - :code:`event_source`
       - Specifies whether the triggered event originated in the browser or on the server.
       - string
       - :code:`browser`, :code:`server`
     * - :code:`event_type`
       - The type of event triggered. Values depend on :code:`event_source`
       - string
       - (see below)
     * - :code:`ip`
       - IP address of the user who triggered the event.
       - string
       - 
     * - :code:`page`
       - Page user was visiting when the event was fired.
       - string
       - :code:`$URL`
     * - :code:`session`
       - This key identifies the user's session. May be undefined.
       - string
       - 32 digits
     * - :code:`time`
       - Gives the GMT time at which the event was fired.
       - string	
       - :code:`YYYY-MM-DDThh:mm:ss.xxxxxx`
     * - :code:`username`
       - The username of the user who caused the event to fire. This string is empty for anonymous events (i.e., user not logged in).
       - string
       - 
       

***********
Event Types
***********

This table lists the different event types logged on the edX platform, and describes what each event type represents, which component it originates from, and what :code:`event` fields are associated with it.

Note that there are two main categories of events: events that originated in the browser (in javascript) and events that originated on the server (during the processing of a request). The :code:`event_source` field distinguishes between the two.


  .. list-table::
     :widths: 20 35 10 10 15 10 45
     :header-rows: 1
  
     * - Event Type
       - Description
       - Component
       - Language
       - :code:`event` Fields
       - Type
       - Details
     * - :code:`seq_goto`
       - Fired when a user jumps between units in a sequence.
       - Sequence
       - CoffeeScript/JS
       - :code:`old`
       - integer
       - Index of the unit being jumped from.
     * - 
       - 
       - 
       - 
       - :code:`new`
       - integer
       - Index of the unit being jumped to.
     * - 
       - 
       - 
       - 
       - :code:`id`
       - integer
       - edX ID of the sequence.
     * - :code:`seq_next`
       - Fired when a user navigates to the next unit in a sequence.
       - Sequence
       - CoffeeScript/JS
       - :code:`old`
       - integer
       - Index of the unit being navigated away from.
     * - 
       - 
       - 
       - 
       - :code:`new`
       - integer
       - Index of the unit being navigated to.
     * - 
       - 
       - 
       - 
       - :code:`id`
       - integer
       - edX ID of the sequence.
     * - :code:`seq_prev`
       - Fired when a user navigates to the previous unit in a sequence.
       - Sequence
       - CoffeeScript/JS
       - :code:`old`
       - integer
       - Index of the unit being navigated away from.
     * - 
       - 
       - 
       - 
       - :code:`new`
       - integer
       - Index of the unit being navigated to.
     * - 
       - 
       - 
       - 
       - :code:`id`
       - integer
       - edX ID of the sequence.
     * - :code:`problem_check`
       - Fired when a user wants to check a problem.
       - Capa
       - CoffeeScript/JS
       - 
       - 
       - The :code:`event` field contains the values of all input fields from the problem being checked, styled as GET parameters.
     * - :code:`problem_reset`
       - Fired when a problem is reset.
       - Capa
       - CoffeeScript/JS
       - 
       - 
       -
     * - :code:`problem_show`
       - Fired when a problem is shown.
       - Capa
       - CoffeeScript/JS
       - :code:`problem`
       - string
       - ID of the problem being shown (e.g., i4x://MITx/6.00x/problem/L15:L15_Problem_2). 
     * - :code:`problem_save`
       - Fired when a problem is saved.
       - Capa
       - CoffeeScript/JS
       - 
       - 
       -
     * - :code:`oe_hide_question` / :code:`oe_hide_problem`
       - 
       - Combined Open-Ended
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose prompt is being hidden. 
     * - :code:`peer_grading_hide_question` / :code:`peer_grading_hide_problem`
       - 
       - Peer Grading
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose prompt is being hidden. 
     * - :code:`staff_grading_hide_question` / :code:`staff_grading_hide_problem`
       - 
       - Staff Grading
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose prompt is being hidden.
     * - :code:`oe_show_question` / :code:`oe_show_problem`
       - 
       - Combined Open-Ended
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose prompt is being shown. 
     * - :code:`peer_grading_show_question` / :code:`peer_grading_show_problem`
       - 
       - Peer Grading
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose prompt is being shown. 
     * - :code:`staff_grading_show_question` / :code:`staff_grading_show_problem`
       - 
       - Staff Grading
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose prompt is being shown.
     * - :code:`rubric_select`
       - 
       - Combined Open-Ended
       - CoffeeScript/JS
       - :code:`location`
       - string
       - The location of the question whose rubric is being selected.
     * - 
       - 
       - 
       - 
       - :code:`selection`
       - integer
       - Value selected on rubric.
     * - 
       - 
       - 
       - 
       - :code:`category`
       - integer
       - Rubric category selected.
     * - :code:`oe_show_full_feedback`
       - 
       - Combined Open-Ended
       - CoffeeScript/JS
       - 
       - 
       - 
     * - :code:`oe_show_respond_to_feedback`
       - 
       - Combined Open-Ended
       - CoffeeScript/JS
       - 
       - 
       - 
     * - :code:`oe_[generated_event_type]`
       - This appears to be a "lambda event." The code turns the HTML link text into the name of the event type (this is the generated event type), and appends it to :code:`oe_`
       - Combined Open-Ended
       - CoffeeScript/JS
       - 
       - 
       - 
     * - :code:`oe_feedback_response_selected`
       - 
       - Combined Open-Ended
       - CoffeeScript/JS
       - :code:`value`
       - integer
       - Value selected in the feedback response form.
     * - :code:`eventName`
       - 
       - Videoalpha
       - CoffeeScript/JS
       - 
       - 
       - 
     * - :code:`page_close`
       - This event type originates from within the Logger itself.
       - Logger
       - CoffeeScript/JS
       - 
       - 
       - 
     * - :code:`play_video`
       - Fired on video play.
       - Video
       - CoffeeScript/JS
       - :code:`id`
       - string
       - EdX ID of the video being watched (e.g., i4x-HarvardX-PH207x-video-Simple_Random_Sample).
     * - 
       - 
       - 
       - 
       - :code:`code`
       - string
       - YouTube ID of the video being watched (e.g., FU3fCJNs94Y).
     * - 
       - 
       - 
       - 
       - :code:`currentTime`
       - float
       - Time the video was played at, in seconds.
     * - 
       - 
       - 
       - 
       - :code:`speed`
       - string
       - Video speed in use (i.e., 0.75, 1.0, 1.25, 1.50).
     * - :code:`pause_video`
       - Fired on video pause.
       - Video
       - CoffeeScript/JS
       - :code:`id`
       - string
       - EdX ID of the video being watched.
     * - 
       - 
       - 
       - 
       - :code:`code`
       - string
       - YouTube ID of the video being watched.
     * - 
       - 
       - 
       - 
       - :code:`currentTime`
       - float
       - Time the video was played at, in seconds.
     * - 
       - 
       - 
       - 
       - :code:`speed`
       - string
       - Video speed in use.
     * - :code:`book`
       - Fired when a user is reading a PDF book.
       - PDF Viewer
       - JS
       - :code:`type`
       - string
       - 'gotopage', 'prevpage', 'nextpage'
     * - 
       - 
       - 
       - 
       - :code:`old`
       - integer
       - Original page number.
     * - 
       - 
       - 
       - 
       - :code:`new`
       - integer
       - Destination page number.
     * - :code:`showanswer` / :code:`show_answer` 
       - Server-side event which displays the answer to a problem.
       - Capa Module
       - Python
       - :code:`problem_id`
       - string
       - EdX ID of the problem being shown.
     * - :code:`problem_check_fail`
       - 
       - Capa Module
       - Python
       - :code:`state`
       - string / JSON
       - Current problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being checked.
     * - 
       - 
       - 
       - 
       - :code:`answers`
       - dict
       - 
     * - 
       - 
       - 
       - 
       - :code:`failure`
       - string
       - 'closed', 'unreset'
     * - :code:`problem_check` / :code:`save_problem_check`
       - Server-side event fired when a problem is checked.
       - Capa Module
       - Python
       - :code:`state`
       - string / JSON
       - Current problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being checked.
     * - 
       - 
       - 
       - 
       - :code:`answers`
       - dict
       - 
     * - 
       - 
       - 
       - 
       - :code:`correct_map`
       - string / JSON
       -  .. list-table::
             :widths: 15 10 15 10
             :header-rows: 1
 
             * - :code:`correct_map` field
               - Type
               - Values / Format
               - Null Allowed?
             * - :code:`answer_id`
               - string
               -
               -
             * - :code:`correctness`
               - string
               - 'correct', 'incorrect'
               -
             * - :code:`npoints`
               - integer
               - Points awarded for this :code:`answer_id`.
               - yes
             * - :code:`correctness`
               - string
               - 'correct', 'incorrect'
               -
             * - :code:`msg`
               - string
               - Gives extra message response.
               -
             * - :code:`hint`
               - string
               - Gives optional hint.
               - yes
             * - :code:`hintmode`
               - string
               - None, 'on_request', 'always'
               - yes
             * - :code:`queuestate`
               - dict
               - None when not queued, else {key:' ', time:' '} where key is a secret string and time is a string dump of a DateTime object of the form '%Y%m%d%H%M%S'.
               - yes
     * - 
       - 
       - 
       - 
       - :code:`success`
       - string
       - 'correct', 'incorrect'
     * - 
       - 
       - 
       - 
       - :code:`attempts`
       - integer
       -
     * - :code:`problem_rescore_fail`
       - 
       - Capa Module
       - Python
       - :code:`state`
       - string / JSON
       - Current problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being rescored.
     * - 
       - 
       - 
       - 
       - :code:`failure`
       - string
       - 'unsupported', 'unanswered', 'input_error', 'unexpected'
     * - :code:`problem_rescore`
       - 
       - Capa Module
       - Python
       - :code:`state`
       - string / JSON
       - Current problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being rescored.
     * - 
       - 
       - 
       - 
       - :code:`orig_score`
       - integer
       - 
     * - 
       - 
       - 
       - 
       - :code:`orig_total`
       - integer
       - 
     * - 
       - 
       - 
       - 
       - :code:`new_score`
       - integer
       - 
     * - 
       - 
       - 
       - 
       - :code:`new_total`
       - integer
       - 
     * - 
       - 
       - 
       - 
       - :code:`correct_map`
       - string / JSON
       - (See above.)
     * - 
       - 
       - 
       - 
       - :code:`success`
       - string
       - 'correct', 'incorrect'
     * - 
       - 
       - 
       - 
       - :code:`attempts`
       - integer
       -
     * - :code:`save_problem_fail`
       - 
       - Capa Module
       - Python
       - :code:`state`
       - string / JSON
       - Current problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being saved.
     * - 
       - 
       - 
       - 
       - :code:`failure`
       - string
       - 'closed', 'done'
     * - 
       - 
       - 
       - 
       - :code:`answers`
       - dict
       -
     * - :code:`save_problem_success`
       - 
       - Capa Module
       - Python
       - :code:`state`
       - string / JSON
       - Current problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being saved.
     * - 
       - 
       - 
       - 
       - :code:`answers`
       - dict
       -
     * - :code:`reset_problem_fail`
       - 
       - Capa Module
       - Python
       - :code:`old_state`
       - string / JSON
       - Current (?) problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being reset.
     * - 
       - 
       - 
       - 
       - :code:`failure`
       - string
       - 'closed', 'not_done'
     * - :code:`reset_problem_fail`
       - 
       - Capa Module
       - Python
       - :code:`old_state`
       - string / JSON
       - Current (?) problem state.
     * - 
       - 
       - 
       - 
       - :code:`problem_id`
       - string
       - ID of the problem being reset.
     * - 
       - 
       - 
       - 
       - :code:`new_state`
       - string / JSON
       - New current (?) problem state.


































