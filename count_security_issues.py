#!/usr/bin/env python3
import json

# Load the JSON file
with open('sonar-4.json', 'r') as f:
    data = json.load(f)

# Create a dictionary of rules with security impact
security_rules = {}
for rule in data['rules']:
    # Check if any impact has softwareQuality as SECURITY
    has_security_impact = any(
        impact.get('softwareQuality') == 'SECURITY' 
        for impact in rule.get('impacts', [])
    )
    if has_security_impact:
        security_rules[rule['id']] = rule

# Count issues that match security rules
security_issue_count = 0
security_issues = []

for issue in data['issues']:
    if issue.get('ruleId') in security_rules:
        security_issue_count += 1
        security_issues.append({
            'ruleId': issue['ruleId'],
            'file': issue.get('primaryLocation', {}).get('filePath', 'Unknown'),
            'line': issue.get('primaryLocation', {}).get('textRange', {}).get('startLine', 'Unknown')
        })

print(f"Total number of security issues: {security_issue_count}")
print(f"\nSecurity rules found ({len(security_rules)}):")
for rule_id, rule in security_rules.items():
    print(f"  - {rule_id}: {rule['name']}")

if security_issue_count > 0:
    print(f"\nAll {security_issue_count} security issues:")
    for i, issue in enumerate(security_issues, 1):
        print(f"  {i}. Rule: {issue['ruleId']}, File: {issue['file']}, Line: {issue['line']}")