from locators import target_locators, snkrs_locators

site_locators = {
    "target": target_locators,
    "snkrs": snkrs_locators
}

def get_locators(site, page):
    """Fetch locators for a given site and page."""
    try:
        return getattr(site_locators[site], page)
    except KeyError:
        raise ValueError(f"Locators for site '{site}' and page '{page}' are not defined.")
