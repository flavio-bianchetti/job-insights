import csv


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    try:
        with open(path, encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=',')
            header, *data = file_reader
            index = header.index('job_type')
            result = []
            for row in data:
                if row[index] not in result:
                    result.append(row[index])
            return result
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    try:
        with open(path, encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=',')
            header, *data = file_reader
            index = header.index('industry')
            result = []
            for row in data:
                if row[index] not in result and row[index]:
                    result.append(row[index])
            return result
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job['industry'] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    try:
        with open(path, encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=',')
            header, *data = file_reader
            index = header.index('max_salary')
            result = 0
            for row in data:
                if row[index].isnumeric() and int(row[index]) > result:
                    result = int(row[index])
            return (result)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    try:
        with open(path, encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=',')
            header, *data = file_reader
            index = header.index('min_salary')
            result = get_max_salary(path)
            for row in data:
                if row[index].isnumeric() and int(row[index]) < result:
                    result = int(row[index])
            return (result)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min = isinstance(job["min_salary"], int)
        max = isinstance(job["max_salary"], int)
        sal = isinstance(salary, int)

        if not (min and max and sal):
            raise ValueError("Numeric type are required")

        if job["min_salary"] > job["max_salary"]:
            raise ValueError("'min_salary' must be less than 'max_salary'")

        return job["min_salary"] <= salary <= job["max_salary"]

    except KeyError:
        raise ValueError("params required")


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    try:

        jobs_list = [
            job
            for job in jobs
            if (
                isinstance(job["min_salary"], int)
                and isinstance(job["max_salary"], int)
                and isinstance(salary, int)
                and job["min_salary"] < job["max_salary"]
            )
        ]

        return [job for job in jobs_list if matches_salary_range(job, salary)]

    except KeyError:
        raise ValueError("params required")
