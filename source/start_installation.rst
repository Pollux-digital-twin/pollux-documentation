.. _installation:

Installation
===========================

POLLUX Digital Twin is compiled as docker container, thus it will be easy to setup and replicate to
a server (on premises or cloud). It is needed to have a basic knowledge of Docker to install this tool.
Several tutorial can be found in the internet (`example <https://medium.com/@sayalishewale12/docker-compose-and-essential-commands-the-ultimate-guide-to-streamlining-your-container-workflow-8018ca171300>`_)

The pre-requisite software of this installation are:

* Docker Desktop (https://docs.docker.com/engine/install/)
* Docker Compose (https://docs.docker.com/compose/install/)

docker-compose.yml (Beta Version)
 .. code-block::
    :linenos:

    networks:
        pollux:

    services:
        pollux_gui:
            image: ghcr.io/pollux-digital-twin/pollux-user-interface:beta
            ports:
                - 5445:5445
            environment:
                - POLLUX_FRONTEND_PORT=5445
                - POLLUX_MYSQLDB_URL=mysqldb
                - POLLUX_ADMIN_EMAIL=admin@localhost
                - POLLUX_ADMIN_PASSWORD=Admin123456!@#$
            restart: unless-stopped
            volumes:
                - project-db:/opt/pollux-project
                - doc-db:/opt/pollux-documentation
            depends_on:
                - mysqldb
            networks:
                - pollux

        pollux_project:
            image: ghcr.io/pollux-digital-twin/pollux-project:beta
            restart: unless-stopped
            volumes:
                - project-db:/opt/pollux-project
            networks:
                - pollux

        pollux_doc:
            image: ghcr.io/pollux-digital-twin/pollux-documentation:beta
            restart: unless-stopped
            volumes:
                - doc-db:/opt/pollux-documentation
            networks:
                - pollux

        mysqldb:
            image: mysql:8.0
            ports:
                - 3306:3306
            environment:
                - MYSQL_ROOT_PASSWORD=root
                - MYSQL_DATABASE=polluxdb
            volumes:
                - mysqldb_data-storage:/data/db
                - mysqldb_var_lib-storage:/var/lib/mysql
            restart: unless-stopped
            networks:
                - pollux


    volumes:
        mysqldb_data-storage:
        mysqldb_var_lib-storage:
        project-db:
        doc-db:



There are several services in this docker-compose.yml file:

#. POLLUX User interface (GUI)
    This container provides the web user interface of POLLUX. This container depends on MySQLDB container
    to access user authentication and project. The port number can be defined in POLLUX_FRONTEND_PORT
    environment variable. The container shares volume of project-db with other container to have a
    common project data and volume of doc-db to access the documentation.


#. POLLUX Project
    This container provides the shared volume project-db that can be accessed by POLLUX Framework
    container and POLLUX User Interface container.

#. POLLUX Documentation
    This container provides the web-based documentation of POLLUX. The content is shared with POLLUX
    User Interface container.

#. MySQLDB
    It is an open-source relational database management system. To handle several data structured of
    POLLUX.








