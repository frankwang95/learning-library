import abc


class WorkBlockGenerator(object):
    """ A class definition for a work block generator by a Scheduler in the lib_learning.collection paradigm to
        generate new work blocks to be forwarded to an Interface.
    """


    @abc.abstractmethod
    def get_next(self, **kwargs):
        """ A method which should be used to get the next work block from the generators internal state. The required
            arguments to this method will vary by application.

        Inputs:
            **kwargs: The implementation should define the required arguments for this method.

        Returns:
            <dict>
        """
        return kwargs


    @abc.abstractmethod
    def reset(self, block):
        """ This method can be defined to determine how to reset the internal state of the generator given a task
            failure. By default, such an operation must be achievable given only the failed work block.

        Inputs:
            block <dict>: A work block previously generated by the generator.
        """
        pass


    @abbc.abstractmethod
    def update(self, block):
        """ In applications where the work block generator needs to make use of information from the workers, this
            can be defined. When a job is found to be completed by the scheduler, this method will be called with the
            sucessful block passed in as the argument.

        Inputs:
        block <dict>: A work block previous generated by the generator.
        """
        pass
