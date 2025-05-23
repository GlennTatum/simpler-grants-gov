"""Mock data output of the roadmap data used in snapshot tests."""

from unittest.mock import Mock


def mock_graphql_roadmap_data(
    _login=Mock,  # noqa: ANN001
    _project=Mock,  # noqa: ANN001
    _quad_field=Mock,  # noqa: ANN001
    _pillar_field=Mock,  # noqa: ANN001
) -> list[dict]:
    """Mock input for snapshot testing of roadmap data."""
    return [
        {
            "content": {
                "title": "Search *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2200",
                "issueType": {
                    "name": "Deliverable",
                },
                "closed": True,
                "createdAt": "2024-09-24T22:55:24Z",
                "closedAt": "2024-12-12T19:05:18Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "55b66bce", "name": "🔎 SimplerFind"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Opportunity Listing *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2203",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-09-25T14:42:58Z",
                "closedAt": "2024-12-12T19:06:27Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "55b66bce", "name": "🔎 SimplerFind"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Engagement Sessions *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2204",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-09-25T14:55:08Z",
                "closedAt": "2024-12-12T19:08:13Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "cd37a2ba", "name": "💬 SimplerEngagement"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Account creation workflow (design)",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2213",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-09-25T15:33:11Z",
                "closedAt": "2024-11-06T03:22:20Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "1f906333", "name": "📋 SimplerApply"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Simpler.Grants.gov brand launch",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2214",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-09-25T15:37:47Z",
                "closedAt": "2025-01-09T00:51:37Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "3801e3d7", "name": "⚙ SimplerPlatform"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Quad 1 Big Demo",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2215",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-09-25T15:54:30Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "cd37a2ba", "name": "💬 SimplerEngagement"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Public Metabase Dashboard",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2225",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-09-26T14:33:14Z",
                "closedAt": "2025-02-03T20:17:49Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "81d7c2d1", "name": "📊 SimplerReporting"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Translation of a static site page",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2226",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-09-26T14:36:46Z",
                "closedAt": "2025-01-17T16:58:20Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "3801e3d7", "name": "⚙ SimplerPlatform"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Cross-program delivery metrics",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2347",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-10-03T15:21:29Z",
                "closedAt": "2025-01-09T21:17:34Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "81d7c2d1", "name": "📊 SimplerReporting"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Cross-program product strategy (Quad 2)",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2356",
                "issueType": {"name": "Deliverable"},
                "closed": True,
                "createdAt": "2024-10-03T19:15:09Z",
                "closedAt": "2025-02-06T04:06:33Z",
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "a9197c86", "name": "SimplerDelivery"},
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Cross-program collaboration tools",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2348",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-10-03T15:30:36Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "a9197c86", "name": "SimplerDelivery"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Cross-program team health",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2357",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-10-03T19:16:37Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "93412e1c",
                "title": "Quad 1.1",
                "startDate": "2024-09-09",
                "duration": 122,
            },
            "pillar": {"optionId": "a9197c86", "name": "SimplerDelivery"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Authenticate via Login.gov",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2640",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-10-29T20:11:33Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "1f906333", "name": "📋 SimplerApply"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "[Team health] Nava Team Retro Feedback",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2658",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-10-29T21:35:50Z",
                "closedAt": None,
                "parent": {
                    "title": "Cross-program team health",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2357",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "Draft email content for participants",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2763",
                "issueType": {"name": "Task"},
                "closed": True,
                "createdAt": "2024-11-07T16:18:06Z",
                "closedAt": "2024-11-12T15:51:04Z",
                "parent": {
                    "title": "Search API Engagement",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2719",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "[DRAFT] Save and Subscribe to a Search - Not Ready for Feedback",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2820",
                "issueType": {"name": "Task"},
                "closed": True,
                "createdAt": "2024-11-13T00:38:44Z",
                "closedAt": "2024-11-25T23:24:33Z",
                "parent": None,
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Search/Opportunity Listing v2 *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2875",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-11-15T19:05:45Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "55b66bce", "name": "🔎 SimplerFind"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Grant protocol specification *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2901",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-11-18T18:48:55Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "3801e3d7", "name": "⚙ SimplerPlatform"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Full Support for Opportunity Attachments (NOFOs) *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3045",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-11-26T18:19:08Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "55b66bce", "name": "🔎 SimplerFind"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Simpler Application Workflow *",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3348",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-12-20T21:36:27Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "1f906333", "name": "📋 SimplerApply"},
            "status": {"optionId": "47fc9ee4", "name": "Planning"},
        },
        {
            "content": {
                "title": "Delivery metrics 2.0",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3377",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2025-01-02T16:39:09Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "81d7c2d1", "name": "📊 SimplerReporting"},
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "Program-level KPIs",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2902",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-11-18T18:57:35Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "81d7c2d1", "name": "📊 SimplerReporting"},
            "status": {"optionId": "53f1247f", "name": "Prioritized"},
        },
        {
            "content": {
                "title": "NOFO builder migration",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2227",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-09-26T14:38:45Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": None,
            "pillar": {"optionId": "48a38cf7", "name": "📣 SimplerNOFOs"},
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "[DRAFT] Launch the CDN",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3174",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-12-10T21:46:32Z",
                "closedAt": None,
                "parent": {
                    "title": "Simpler.Grants.gov Program Work Catch-all",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/3109",
                },
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": None,
            "status": {"optionId": "5ec0120a", "name": "In Progress"},
        },
        {
            "content": {
                "title": "[DRAFT] Automated cross-program dependency mapping",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2903",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-11-18T20:06:50Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": None,
            "pillar": {"optionId": "a9197c86", "name": "SimplerDelivery"},
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "[Team health] Survey",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2946",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-11-20T16:17:59Z",
                "closedAt": None,
                "parent": {
                    "title": "Cross-program team health",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2357",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "[Team health] Recognition forum",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2947",
                "issueType": {"name": "Epic"},
                "closed": True,
                "createdAt": "2024-11-20T16:25:58Z",
                "closedAt": "2024-12-26T21:09:21Z",
                "parent": {
                    "title": "Cross-program team health",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2357",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "[Product strategy] Dependency tracking",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2951",
                "issueType": {"name": "Epic"},
                "closed": True,
                "createdAt": "2024-11-20T16:42:38Z",
                "closedAt": "2025-01-21T15:06:41Z",
                "parent": {
                    "title": "Cross-program product strategy (Quad 2)",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2356",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "Open Source Community Growth",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3314",
                "issueType": {"name": "Deliverable"},
                "closed": False,
                "createdAt": "2024-12-19T17:30:27Z",
                "closedAt": None,
                "parent": None,
            },
            "quad": {
                "iterationId": "f5ce525b",
                "title": "Quad 1.2",
                "startDate": "2025-01-09",
                "duration": 120,
            },
            "pillar": {"optionId": "cd37a2ba", "name": "💬 SimplerEngagement"},
            "status": {"optionId": "47fc9ee4", "name": "Planning"},
        },
        {
            "content": {
                "title": "SGG/Login.Gov Integration (API <-> Login.gov)",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2642",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-10-29T20:16:01Z",
                "closedAt": None,
                "parent": {
                    "title": "Authenticate via Login.gov",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2640",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "SGG/Login.Gov Integration (Next.js <-> API)",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2643",
                "issueType": {"name": "Epic"},
                "closed": True,
                "createdAt": "2024-10-29T20:17:59Z",
                "closedAt": "2025-01-13T17:14:09Z",
                "parent": {
                    "title": "Authenticate via Login.gov",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2640",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "98236657", "name": "Done"},
        },
        {
            "content": {
                "title": "SGG/Login.gov Integration Design",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/2745",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-11-06T04:08:19Z",
                "closedAt": None,
                "parent": {
                    "title": "Authenticate via Login.gov",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2640",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "Make attachment files available via the API",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3046",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-11-26T18:31:16Z",
                "closedAt": None,
                "parent": {
                    "title": "Full Support for Opportunity Attachments (NOFOs) *",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/3045",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "Enable users to download opportunity attachments",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3048",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-11-26T18:38:51Z",
                "closedAt": None,
                "parent": {
                    "title": "Full Support for Opportunity Attachments (NOFOs) *",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/3045",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "CDN",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3092",
                "issueType": {"name": "Epic"},
                "closed": True,
                "createdAt": "2024-12-03T21:09:12Z",
                "closedAt": "2024-12-03T21:10:00Z",
                "parent": None,
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": "Contact Us Management & Info for Grants.gov Cust Support ",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3110",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-12-04T23:54:10Z",
                "closedAt": None,
                "parent": {
                    "title": "Simpler.Grants.gov Program Work Catch-all",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/3109",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": {
                "title": """Enable users to save an opportunity and
                  view/delete their saved opportunities""",
                "url": "https://github.com/HHS/simpler-grants-gov/issues/3118",
                "issueType": {"name": "Epic"},
                "closed": False,
                "createdAt": "2024-12-06T00:51:29Z",
                "closedAt": None,
                "parent": {
                    "title": "Search/Opportunity Listing v2 *",
                    "url": "https://github.com/HHS/simpler-grants-gov/issues/2875",
                },
            },
            "quad": None,
            "pillar": None,
            "status": {"optionId": "f75ad846", "name": "Backlog"},
        },
        {
            "content": None,
            "status": None,
            "sprint": None,
            "points": None,
            "quad": None,
            "pillar": None,
        },
    ]
