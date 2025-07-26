class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = {}

        for visit_domain in cpdomains:

            visit, domain = visit_domain.split()
            visit = int(visit)

            subdomains = domain.split('.')
            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])

                if visit_count.get(subdomain) is not None:
                    visit_count[subdomain] += visit

                else:
                    visit_count[subdomain] = visit

        return [f'{visit} {domain}' for domain, visit in visit_count.items()]
