#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 00:16:52 2023

@author: Baudouin
"""

import streamlit as st

tools = {
    "Notion": {
        "description": "Notion is an all-in-one workspace tool that has become very popular for personal and business use. It is a tool that allows users to create a database of information, as well as organize, manage, and collaborate on that information. Notion is known for its flexibility and versatility, as it can be used for a wide range of purposes, from personal note-taking to team project management.\n\nSome of the most popular features of Notion include:\n\n- Pages and sub-pages: Users can create pages and sub-pages to organize their information. These pages can contain various types of content, such as text, images, videos, and more.\n- Templates: Notion offers a wide range of templates for different purposes, such as project management, note-taking, and personal finance. These templates can help users get started quickly and easily, and they can be customized to suit individual needs.\n- Databases: Notion allows users to create databases for storing and organizing information. These databases can be customized to include different types of fields, such as text, date, number, and more.\n- Kanban boards: Notion offers Kanban boards, which are useful for visualizing tasks and projects in progress. Users can move tasks between columns to indicate their status.\n- Collaboration: Notion makes it easy for teams to collaborate on projects by allowing them to share pages and databases. Users can also comment on pages and tag other users to notify them.\n- Integrations: Notion integrates with a variety of other tools, such as Google Drive, Trello, and Slack, making it easy to connect and sync information across different platforms.\n\nSome of the usual use cases of Notion include:\n\n- Personal note-taking: Notion can be used as a personal note-taking tool, allowing users to create a database of information for their own use.\n- Project management: Notion is useful for managing projects, as it allows users to create pages and databases for different tasks and projects.\n- Team collaboration: Notion is great for team collaboration, as it allows team members to share information and work together on projects.\n- Knowledge management: Notion is useful for organizing and managing knowledge, as it allows users to create a database of information that can be easily searched and accessed.\n\nSome of the benefits of using Notion include:\n\n- Flexibility: Notion is very flexible and can be used for a wide range of purposes.\n- Customizability: Notion allows users to customize pages, databases, and templates to suit their individual needs.\n- Collaboration: Notion makes it easy for teams to collaborate on projects, allowing them to share information and work together.\n- Integrations: Notion integrates with a variety of other tools, making it easy to connect and sync information across different platforms.\n\nSome of the drawbacks of using Notion include:\n\n- Complexity: Notion can be overwhelming for new users, as it has many features and options.\n- Cost: Notion is not a free tool, and users must pay for access to certain features and integrations.\n- Performance issues: Notion can be slow to load and use, especially when working with large databases or pages.\n\nOverall, Notion is a powerful tool that can be used for a variety of purposes. Its flexibility, customizability, and collaboration features make it a popular choice for personal and business use. However, its complexity, cost, and performance issues may make it less suitable for some users.",
        "website": "https://www.notion.so/"
    },
    "Airtable": {
        "description": """Airtable is a cloud-based spreadsheet and database management tool that combines the features of a traditional spreadsheet with the power of a relational database. It offers a flexible and user-friendly interface, making it easy for users to manage and organize their data.

Some of the most popular features of Airtable include:

- Customizable fields: Airtable allows users to create custom fields for their data, including text, numbers, dates, attachments, and more. This makes it easy to tailor the database to specific needs.
- Templates: Airtable offers a variety of templates for different use cases, such as project management, event planning, and sales tracking. These templates can be customized to fit individual needs.
- Collaborative features: Airtable allows teams to work together on projects, share databases, and comment on records. It also has a built-in chat feature for real-time collaboration.
- Integrations: Airtable integrates with a variety of other tools, such as Slack, Zapier, and Google Drive, making it easy to connect and sync information across different platforms.
- Views: Airtable offers different views of the data, including grid view, calendar view, and kanban view. This allows users to visualize their data in different ways.

Some of the usual use cases of Airtable include:

- Project management: Airtable is great for managing projects, as it allows users to track tasks, deadlines, and progress. It can also be used to assign tasks to team members and monitor their status.
- Event planning: Airtable is useful for organizing and managing events, as it allows users to track attendees, vendors, and other important details.
- CRM: Airtable can be used as a simple customer relationship management tool, allowing users to track customer interactions, sales leads, and more.
- Inventory management: Airtable is useful for tracking inventory, as it allows users to keep track of stock levels, reorder quantities, and suppliers.

Some of the benefits of using Airtable include:

- User-friendly interface: Airtable has a simple and intuitive interface that is easy to navigate.
- Customizability: Airtable allows users to create custom fields, templates, and views to fit their specific needs.
- Collaboration: Airtable makes it easy for teams to work together on projects and share information.
- Integrations: Airtable integrates with a variety of other tools, making it easy to connect and sync information across different platforms.

Some of the drawbacks of using Airtable include:

- Cost: Airtable is not a free tool, and users must pay for access to certain features and integrations.
- Limited features: While Airtable offers many features, it may not be as robust as some other database management tools.
- Performance issues: Airtable can be slow to load and use, especially when working with large databases or complex formulas.

Overall, Airtable is a powerful tool that combines the best of spreadsheets and databases. Its customizable fields, templates, and collaborative features make it a popular choice for personal and business use. However, its cost and performance issues may make it less suitable for some users.""",
        "website": "https://airtable.com/"
    },
    "Make": {
        "description": """
Make is a no-code platform that allows users to create custom workflows and automate tasks without writing code. With Make, users can connect to various apps and services to create powerful workflows that can save time and increase productivity.

Some of the most popular features of Make include:

- Integration with various apps and services: Make can connect to a variety of apps and services, including Google Drive, Slack, Trello, and more, allowing users to create workflows that incorporate these tools.
- Drag-and-drop interface: Make's intuitive drag-and-drop interface makes it easy to create workflows, even for users with no coding experience.
- Customizable templates: Make offers customizable templates that users can use as a starting point for their workflows.
- Built-in actions: Make comes with built-in actions that can be used to automate common tasks, such as sending emails, creating calendar events, and more.
- Conditional logic: Make allows users to set up conditional logic, which can be used to create more complex workflows that take into account different scenarios.
- Scheduled workflows: Users can schedule workflows to run at specific times or intervals, making it easy to automate recurring tasks.

Some of the usual use cases of Make include:

- Sales and marketing automation: Make can be used to automate tasks such as lead generation, lead nurturing, and email marketing.
- Project management: Make can be used to create workflows that help manage projects, including tasks such as assigning tasks, sending notifications, and more.
- HR processes: Make can be used to automate HR processes such as onboarding, offboarding, and performance reviews.
- Data management: Make can be used to automate data-related tasks such as data cleaning, merging, and analysis.

Some of the benefits of using Make include:

- Increased productivity: By automating repetitive tasks, Make can save users time and increase productivity.
- No coding required: Make's no-code platform means that users with no coding experience can create powerful workflows.
- Integration with other tools: Make can be integrated with a variety of other tools, making it easy to incorporate into existing workflows and processes.
- Scalability: Make can be used to create workflows of any size, from small tasks to complex processes.

Some of the drawbacks of using Make include:

- Limited customization: While Make's customizable templates can be a great starting point, users may find that they are limited in terms of customization options.
- Learning curve: While Make's drag-and-drop interface is intuitive, users may still need to spend some time learning how to use the platform effectively.
- Cost: Make is not a free tool, and users must pay for access to certain features and integrations.

Overall, Make is a powerful tool that can be used to automate tasks and increase productivity without writing code. Its intuitive interface, customizable templates, and built-in actions make it a popular choice for users with no coding experience, but its limited customization options and cost may be drawbacks for some users.
""",
        "website": "https://www.make.so/"
    },
    "Bubble": {
        "description": "Bubble is a no-code platform that enables users to design and launch web applications without writing code. It offers a **drag-and-drop interface**, a wide range of **templates**, and a powerful set of features for building **complex web applications**. Some of the **popular features** of Bubble include:\n\n- **Visual workflows**\n- **Responsive design**\n- **Built-in database**\n- **User authentication and roles**\n- **Payment integrations**\n- **Custom domains**\n\nBubble is commonly used for **building web applications without coding**, creating **prototypes and MVPs**, developing **internal tools and dashboards**, building **e-commerce websites**, and creating **marketplaces and social networks**. Some of the **benefits** of using Bubble include:\n\n- **No coding required**\n- **Rapid development and prototyping**\n- Powerful set of features for building **complex applications**\n- **Flexible design and customization options**\n- Integration with **third-party services and APIs**\n- No need for separate hosting or infrastructure\n\nHowever, there are also some **drawbacks** to consider, such as the **learning curve for advanced features**, limited control over **underlying code**, higher pricing for more advanced features, limited **SEO optimization**, and may not be suitable for very large or complex applications.",
        "website": "https://bubble.io/"
    },
    "Webflow": {
        "description": "**Webflow** is a no-code platform for designing, building, and launching responsive websites. With its intuitive drag-and-drop interface, extensive design tools, and powerful CMS, Webflow empowers users to create custom websites without writing any code. \n\nSome of the most popular features of Webflow include:\n\n- Drag-and-drop interface\n- Responsive design\n- Extensive design tools (e.g., animations, interactions, CMS)\n- E-commerce functionality\n- Hosting and site management\n- Integration with third-party tools (e.g., Zapier, Google Analytics)\n\nSome of the usual use cases for Webflow include:\n\n- Creating custom websites for businesses and organizations\n- Building landing pages and marketing sites\n- Developing e-commerce stores\n- Prototyping and testing new website ideas\n\nSome benefits of using Webflow include:\n\n- No coding required\n- Extensive design capabilities\n- Responsive and flexible design\n- Built-in e-commerce functionality\n- Integration with third-party tools\n\nSome drawbacks of using Webflow include:\n\n- Steep learning curve for more advanced features\n- Limited control over underlying code\n- Higher pricing for more advanced features\n- Limited support for complex or dynamic functionality\n",
        "website": "https://webflow.com/"
    }
}

# Create a function that displays information about a specific tool
def display_tool(tool_name):
    tool = tools[tool_name]
    st.write(f"# {tool_name}")
    st.write(tool["description"])
    st.write(f"Check out their website: {tool['website']}")

# Create the Streamlit app
st.write("# No-Code Tools")
st.write("This app provides information about popular no-code tools.")

# Create a selectbox for choosing a tool
tool_name = st.selectbox("Select a tool", list(tools.keys()))

# Display information about the chosen tool
display_tool(tool_name)


