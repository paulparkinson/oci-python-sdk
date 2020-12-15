# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverEntitlement(object):
    """
    Information about a RoverEntitlement.
    """

    #: A constant which can be used with the lifecycle_state property of a RoverEntitlement.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RoverEntitlement.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RoverEntitlement.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RoverEntitlement.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new RoverEntitlement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tenant_id:
            The value to assign to the tenant_id property of this RoverEntitlement.
        :type tenant_id: str

        :param id:
            The value to assign to the id property of this RoverEntitlement.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RoverEntitlement.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this RoverEntitlement.
        :type display_name: str

        :param requestor_name:
            The value to assign to the requestor_name property of this RoverEntitlement.
        :type requestor_name: str

        :param requestor_email:
            The value to assign to the requestor_email property of this RoverEntitlement.
        :type requestor_email: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RoverEntitlement.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param entitlement_details:
            The value to assign to the entitlement_details property of this RoverEntitlement.
        :type entitlement_details: str

        :param lifecycle_state_details:
            The value to assign to the lifecycle_state_details property of this RoverEntitlement.
        :type lifecycle_state_details: str

        :param time_created:
            The value to assign to the time_created property of this RoverEntitlement.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RoverEntitlement.
        :type time_updated: datetime

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RoverEntitlement.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RoverEntitlement.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RoverEntitlement.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'tenant_id': 'str',
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'requestor_name': 'str',
            'requestor_email': 'str',
            'lifecycle_state': 'str',
            'entitlement_details': 'str',
            'lifecycle_state_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'tenant_id': 'tenantId',
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'requestor_name': 'requestorName',
            'requestor_email': 'requestorEmail',
            'lifecycle_state': 'lifecycleState',
            'entitlement_details': 'entitlementDetails',
            'lifecycle_state_details': 'lifecycleStateDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._tenant_id = None
        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._requestor_name = None
        self._requestor_email = None
        self._lifecycle_state = None
        self._entitlement_details = None
        self._lifecycle_state_details = None
        self._time_created = None
        self._time_updated = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def tenant_id(self):
        """
        Gets the tenant_id of this RoverEntitlement.
        tenant Id.


        :return: The tenant_id of this RoverEntitlement.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this RoverEntitlement.
        tenant Id.


        :param tenant_id: The tenant_id of this RoverEntitlement.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RoverEntitlement.
        A property that can uniquely identify the rover entitlement.


        :return: The id of this RoverEntitlement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RoverEntitlement.
        A property that can uniquely identify the rover entitlement.


        :param id: The id of this RoverEntitlement.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RoverEntitlement.
        The compartment Id for the entitlement.


        :return: The compartment_id of this RoverEntitlement.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RoverEntitlement.
        The compartment Id for the entitlement.


        :param compartment_id: The compartment_id of this RoverEntitlement.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this RoverEntitlement.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this RoverEntitlement.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RoverEntitlement.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this RoverEntitlement.
        :type: str
        """
        self._display_name = display_name

    @property
    def requestor_name(self):
        """
        **[Required]** Gets the requestor_name of this RoverEntitlement.
        Requestor name for the entitlement.


        :return: The requestor_name of this RoverEntitlement.
        :rtype: str
        """
        return self._requestor_name

    @requestor_name.setter
    def requestor_name(self, requestor_name):
        """
        Sets the requestor_name of this RoverEntitlement.
        Requestor name for the entitlement.


        :param requestor_name: The requestor_name of this RoverEntitlement.
        :type: str
        """
        self._requestor_name = requestor_name

    @property
    def requestor_email(self):
        """
        **[Required]** Gets the requestor_email of this RoverEntitlement.
        Requestor email for the entitlement.


        :return: The requestor_email of this RoverEntitlement.
        :rtype: str
        """
        return self._requestor_email

    @requestor_email.setter
    def requestor_email(self, requestor_email):
        """
        Sets the requestor_email of this RoverEntitlement.
        Requestor email for the entitlement.


        :param requestor_email: The requestor_email of this RoverEntitlement.
        :type: str
        """
        self._requestor_email = requestor_email

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this RoverEntitlement.
        Lifecyclestate for the entitlement.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RoverEntitlement.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RoverEntitlement.
        Lifecyclestate for the entitlement.


        :param lifecycle_state: The lifecycle_state of this RoverEntitlement.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def entitlement_details(self):
        """
        Gets the entitlement_details of this RoverEntitlement.
        Details about the entitlement.


        :return: The entitlement_details of this RoverEntitlement.
        :rtype: str
        """
        return self._entitlement_details

    @entitlement_details.setter
    def entitlement_details(self, entitlement_details):
        """
        Sets the entitlement_details of this RoverEntitlement.
        Details about the entitlement.


        :param entitlement_details: The entitlement_details of this RoverEntitlement.
        :type: str
        """
        self._entitlement_details = entitlement_details

    @property
    def lifecycle_state_details(self):
        """
        Gets the lifecycle_state_details of this RoverEntitlement.
        A property that can contain details on the lifecycle.


        :return: The lifecycle_state_details of this RoverEntitlement.
        :rtype: str
        """
        return self._lifecycle_state_details

    @lifecycle_state_details.setter
    def lifecycle_state_details(self, lifecycle_state_details):
        """
        Sets the lifecycle_state_details of this RoverEntitlement.
        A property that can contain details on the lifecycle.


        :param lifecycle_state_details: The lifecycle_state_details of this RoverEntitlement.
        :type: str
        """
        self._lifecycle_state_details = lifecycle_state_details

    @property
    def time_created(self):
        """
        Gets the time_created of this RoverEntitlement.
        Time of creation for the entitlement.


        :return: The time_created of this RoverEntitlement.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RoverEntitlement.
        Time of creation for the entitlement.


        :param time_created: The time_created of this RoverEntitlement.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RoverEntitlement.
        Time when the entitlement was last updated.


        :return: The time_updated of this RoverEntitlement.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RoverEntitlement.
        Time when the entitlement was last updated.


        :param time_updated: The time_updated of this RoverEntitlement.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RoverEntitlement.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RoverEntitlement.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RoverEntitlement.
        The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RoverEntitlement.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RoverEntitlement.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RoverEntitlement.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RoverEntitlement.
        The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RoverEntitlement.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RoverEntitlement.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this RoverEntitlement.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RoverEntitlement.
        The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined and scoped to namespaces.
        For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this RoverEntitlement.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other