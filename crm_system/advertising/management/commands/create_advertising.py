from django.core.management import BaseCommand

from services.models import Service
from advertising.models import AdvertisingCompany


class Command(BaseCommand):
    """Creates advertising"""

    def handle(self, *args, **options):
        self.stdout.write("Start of advertising creation")

        advertising_data = [
            {
                "title": "Website Development Special Offer",
                "promotion_channel": "Google Ads",
                "budget": 1500,
                "service_title": "Website Development",
            },
            {
                "title": "Mobile App Launch Campaign",
                "promotion_channel": "Facebook Ads",
                "budget": 2000,
                "service_title": "Mobile App Development",
            },
            {
                "title": "Boost Your Online Visibility - SEO",
                "promotion_channel": "Google Search Ads",
                "budget": 1000,
                "service_title": "IT Infrastructure Support and Maintenance",
            },
            {
                "title": "IT Consulting - Digital Transformation",
                "promotion_channel": "LinkedIn Ads",
                "budget": 1200,
                "service_title": "SEO Optimization",
            },
            {
                "title": "Enhance Your Business with Custom Software",
                "promotion_channel": "Instagram Ads",
                "budget": 1800,
                "service_title": "IT Consulting",
            },
            {
                "title": "Cloud Solutions for Scalability",
                "promotion_channel": "Twitter Ads",
                "budget": 1400,
                "service_title": "Software Development",
            },
            {
                "title": "Secure Your Business - Cybersecurity",
                "promotion_channel": "Google Display Network",
                "budget": 1600,
                "service_title": "Third-party Service Integration",
            },
            {
                "title": "Get a CRM System for Better Sales",
                "promotion_channel": "Facebook Ads",
                "budget": 1500,
                "service_title": "Cloud Solutions",
            },
            {
                "title": "Optimize Your IT Infrastructure",
                "promotion_channel": "LinkedIn Ads",
                "budget": 1300,
                "service_title": "Cybersecurity",
            },
            {
                "title": "Third-party Service Integration Promo",
                "promotion_channel": "Twitter Ads",
                "budget": 1100,
                "service_title": "CRM System Development and Implementation",
            },
            {
                "title": "Mobile App Development for Your Business",
                "promotion_channel": "Google Ads",
                "budget": 2000,
                "service_title": "Mobile App Development",
            },
            {
                "title": "Website Development for Small Businesses",
                "promotion_channel": "Instagram Ads",
                "budget": 1000,
                "service_title": "Website Development",
            },
            {
                "title": "IT Infrastructure Support Campaign",
                "promotion_channel": "LinkedIn Ads",
                "budget": 1700,
                "service_title": "Cybersecurity",
            },
            {
                "title": "Boost Your Sales with Custom Software",
                "promotion_channel": "Facebook Ads",
                "budget": 1600,
                "service_title": "IT Consulting",
            },
            {
                "title": "Cloud Solutions for Remote Work",
                "promotion_channel": "Google Search Ads",
                "budget": 1300,
                "service_title": "Software Development",
            },
        ]

        services = Service.objects.all()

        for adv_data in advertising_data:

            try:
                service = services.get(title=adv_data["service_title"])
            except Service.DoesNotExist:
                self.stdout.write("The services were not created in advance")
                return

            advertising, create = AdvertisingCompany.objects.get_or_create(
                title=adv_data["title"],
                promotion_channel=adv_data["promotion_channel"],
                budget=adv_data["budget"],
                service=service,
            )

            self.stdout.write(f"Created advertising: {advertising.title}")

        self.stdout.write(self.style.SUCCESS("Advertising created"))
