define [], () ->
    class StaffGradingBackend
        constructor: (ajax_url, mock_backend) ->
            @ajax_url = ajax_url
            # prevent this from trying to make requests when we don't have
            # a proper url
            if !ajax_url
                mock_backend = true
            @mock_backend = mock_backend
            if @mock_backend
                @mock_cnt = 0

        mock: (cmd, data) ->
            # Return a mock response to cmd and data
            # should take a location as an argument
            if cmd == 'get_next'
                @mock_cnt++
                switch data.location
                    when 'i4x://MITx/3.091x/problem/open_ended_demo1'
                        response =
                            success: true
                            problem_name: 'Problem 1'
                            num_graded: 3
                            min_for_ml: 5
                            num_pending: 4
                            prompt: '''
                                    <h2>S11E3: Metal Bands</h2>
                                    <p>Shown below are schematic band diagrams for two different metals. Both diagrams appear different, yet both of the elements are undisputably metallic in nature.</p>
                                    <img width="480" src="/static/images/LSQimages/shaded_metal_bands.png"/>
                                    <p>* Why is it that both sodium and magnesium behave as metals, even though the s-band of magnesium is filled? </p>
                                    <p>This is a self-assessed open response question. Please use as much space as you need in the box below to answer the question.</p>
                                    '''
                            submission: '''
                                        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.

                                        The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
                                        '''
                            rubric: '''
                                    <table class="rubric"><tbody><tr><th>Purpose</th>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-0" id="score-0-0" value="0"><label for="score-0-0">No product</label>
                                    </td>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-0" id="score-0-1" value="1"><label for="score-0-1">Unclear purpose or main idea</label>
                                    </td>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-0" id="score-0-2" value="2"><label for="score-0-2">Communicates an identifiable purpose and/or main idea for an audience</label>
                                    </td>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-0" id="score-0-3" value="3"><label for="score-0-3">Achieves a clear and distinct purpose for a targeted audience and communicates main ideas with effectively used techniques to introduce and represent ideas and insights</label>
                                    </td>
                                    </tr><tr><th>Organization</th>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-1" id="score-1-0" value="0"><label for="score-1-0">No product</label>
                                    </td>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-1" id="score-1-1" value="1"><label for="score-1-1">Organization is unclear; introduction, body, and/or conclusion are underdeveloped, missing or confusing.</label>
                                    </td>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-1" id="score-1-2" value="2"><label for="score-1-2">Organization is occasionally unclear; introduction, body or conclusion may be underdeveloped.</label>
                                    </td>

                                    <td>
                                    <input type="radio" class="score-selection" name="score-selection-1" id="score-1-3" value="3"><label for="score-1-3">Organization is clear and easy to follow; introduction, body and conclusion are defined and aligned with purpose.</label>
                                    </td>
                                    </tr></tbody></table>'''
                            submission_id: @mock_cnt
                            max_score: 2 + @mock_cnt % 3
                            ml_error_info : 'ML accuracy info: ' + @mock_cnt
                    when 'i4x://MITx/3.091x/problem/open_ended_demo2'
                        response =
                            success: true
                            problem_name: 'Problem 2'
                            num_graded: 2
                            min_for_ml: 5
                            num_pending: 4
                            prompt: 'This is a fake second problem'
                            submission: 'This is the best submission ever! ' + @mock_cnt
                            rubric: 'I am a rubric for grading things! ' + @mock_cnt
                            submission_id: @mock_cnt
                            max_score: 2 + @mock_cnt % 3
                            ml_error_info : 'ML accuracy info: ' + @mock_cnt
                    else
                        response =
                            success: false


            else if cmd == 'save_grade'
                response =
                    @mock('get_next', {location: data.location})
                # get_problem_list
                # should get back a list of problem_ids, problem_names, num_graded, min_for_ml
            else if cmd == 'get_problem_list'
                @mock_cnt = 1
                response =
                    success: true
                    problem_list: [
                        {location: 'i4x://MITx/3.091x/problem/open_ended_demo1',
                        problem_name: "Problem 1", num_graded: 3, num_pending: 5, min_for_ml: 10},
                        {location: 'i4x://MITx/3.091x/problem/open_ended_demo2',
                        problem_name: "Problem 2", num_graded: 1, num_pending: 5, min_for_ml: 10}
                    ]
            else
                response =
                    success: false
                    error: 'Unknown command ' + cmd

            if @mock_cnt % 5 == 0
                response =
                    success: true
                    message: 'No more submissions'


            if @mock_cnt % 7 == 0
                response =
                    success: false
                    error: 'An error for testing'

            return response


        post: (cmd, data, callback) ->
            if @mock_backend
                callback(@mock(cmd, data))
            else
                # TODO: replace with postWithPrefix when that's loaded
                $.post(@ajax_url + cmd, data, callback)
                    .error => callback({success: false, error: "Error occured while performing javascript AJAX post."})
