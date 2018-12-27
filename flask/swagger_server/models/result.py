# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Result(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, course: str=None, question_id: str=None):  # noqa: E501
        """Result - a model defined in Swagger

        :param course: The course of this Result.  # noqa: E501
        :type course: str
        :param question_id: The question_id of this Result.  # noqa: E501
        :type question_id: str
        """
        self.swagger_types = {
            'course': str,
            'question_id': str
        }

        self.attribute_map = {
            'course': 'course',
            'question_id': 'question id'
        }

        self._course = course
        self._question_id = question_id

    @classmethod
    def from_dict(cls, dikt) -> 'Result':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Result of this Result.  # noqa: E501
        :rtype: Result
        """
        return util.deserialize_model(dikt, cls)

    @property
    def course(self) -> str:
        """Gets the course of this Result.


        :return: The course of this Result.
        :rtype: str
        """
        return self._course

    @course.setter
    def course(self, course: str):
        """Sets the course of this Result.


        :param course: The course of this Result.
        :type course: str
        """
        if course is None:
            raise ValueError("Invalid value for `course`, must not be `None`")  # noqa: E501

        self._course = course

    @property
    def question_id(self) -> str:
        """Gets the question_id of this Result.


        :return: The question_id of this Result.
        :rtype: str
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id: str):
        """Sets the question_id of this Result.


        :param question_id: The question_id of this Result.
        :type question_id: str
        """
        if question_id is None:
            raise ValueError("Invalid value for `question_id`, must not be `None`")  # noqa: E501

        self._question_id = question_id