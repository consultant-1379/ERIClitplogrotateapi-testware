#!/usr/bin/env python

'''
COPYRIGHT Ericsson 2019
The copyright to the computer program(s) herein is the property of
Ericsson Inc. The programs may be used and/or copied only with written
permission from Ericsson Inc. or in accordance with the terms and
conditions stipulated in the agreement/contract under which the
program(s) have been supplied.

@since:     October 2014
@author:    Maria
@summary:   Integration test to create,remove and update logrotate rules
            Agile: STORY LITPCDS-664
'''

from litp_cli_utils import CLIUtils
from litp_generic_test import GenericTest, attr


class Story664(GenericTest):

    '''
    As a LITP user I want the Logrotate Plug-in to be migrated from LITP 1.x
    so that I can utilise logrotate in LITP 2.x
    '''
    def setUp(self):
        """
        Description:
            Runs before every single test
        Actions:
            1. Call the super class setup method
            2. Set up variables used in the tests
        Results:
            The super class prints out diagnostics and variables
            common to all tests are available.
        """
        # 1. Call super class setup
        super(Story664, self).setUp()
        self.test_ms = self.get_management_node_filename()
        self.cli = CLIUtils()

    def tearDown(self):
        """
        Description:
            Runs after every single test
        Actions:
            1. Perform Test Cleanup
        Results:
            Items used in the test are cleaned up and the
            super class prints out end test diagnostics
        """
        super(Story664, self).tearDown()

    @attr('all', 'revert', 'story664api', 'story664api_tc01')
    def test_01_p_test_api(self):
        """
        @tms_id: litpcds_664_tc01
        @tms_requirements_id: LITPCDS-664
        @tms_title: Verify logrotate api exists
        @tms_description: Verify logrotate item and associated properties
        exist.
        @tms_test_steps:
        @step:  Run show command on '/item-types'
        @result: logrotate-rule-config item exists
        @step:  Run show command on '/item-types'
        @result: logrotate-rule item exists
        @step:  Run show command on '/property-types'
        @result: logrotate properties exist
        @tms_test_precondition: NA
        @tms_execution_type: Automated
        """
        # 1. Check item-type contains logrotate types
        stdout, _, _ = self.execute_cli_show_cmd(self.test_ms, "/item-types")
        self.assertTrue(self.is_text_in_list("logrotate-rule-config", stdout))

        stdout, _, _ = self.execute_cli_show_cmd(self.test_ms, "/item-types")
        self.assertTrue(self.is_text_in_list("logrotate-rule", stdout))

        # 2. Check property-types have been added
        stdout, _, _ = self.execute_cli_show_cmd(
            self.test_ms, "/property-types")
        self.assertTrue(self.is_text_in_list("logrotate_date_format", stdout))
        self.assertTrue(self.is_text_in_list("logrotate_basic_size", stdout))
        self.assertTrue(self.is_text_in_list("logrotate_time_period", stdout))
        self.assertTrue(self.is_text_in_list("logrotate_email", stdout))
