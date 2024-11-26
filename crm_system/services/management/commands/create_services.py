from django.core.management import BaseCommand

from services.models import Service


class Command(BaseCommand):
    """Creates services"""

    def handle(self, *args, **options):
        self.stdout.write("Start of service creation")

        services_data = [
            {
                "title": "Website Development",
                "description": (
                    "Creation and setup of modern websites using the "
                    "latest technologies, tools, and design principles. "
                    "We provide responsive and user-friendly websites "
                    "tailored to your business needs, ensuring high "
                    "performance and scalability. From small landing "
                    "pages to large e-commerce platforms, we handle all "
                    "aspects of development and optimization."
                ),
                "price": 50000,
            },
            {
                "title": "Mobile App Development",
                "description": (
                    "Development of mobile applications for iOS and "
                    "Android platforms, with customized solutions "
                    "designed to meet the specific needs of your "
                    "business. Our team specializes in creating "
                    "intuitive, feature-rich apps that help you engage "
                    "with your customers, increase brand visibility, "
                    "and drive growth in the mobile space."
                ),
                "price": 70000,
            },
            {
                "title": "IT Infrastructure Support and Maintenance",
                "description": (
                    "Comprehensive IT infrastructure support and "
                    "maintenance services to ensure the continuous "
                    "operation of your technology environment. We offer "
                    "proactive monitoring, updates, and troubleshooting, "
                    "as well as security patches and system optimization. "
                    "Our team ensures your systems are always up to date "
                    "and running smoothly, minimizing downtime and "
                    "disruptions."
                ),
                "price": 30000,
            },
            {
                "title": "SEO Optimization",
                "description": (
                    "Search Engine Optimization (SEO) services to "
                    "improve your website's visibility in search engine "
                    "results. We use a combination of on-page and "
                    "off-page strategies to optimize your website for "
                    "relevant keywords, drive more organic traffic, and "
                    "increase conversions. Our SEO experts ensure that "
                    "your site ranks higher, attracts more visitors, "
                    "and meets business goals."
                ),
                "price": 20000,
            },
            {
                "title": "IT Consulting",
                "description": (
                    "IT consulting services that help businesses identify "
                    "the most effective technology solutions to address "
                    "their challenges and achieve their goals. We provide "
                    "strategic advice on technology infrastructure, system "
                    "integration, software development, and digital "
                    "transformation, ensuring you stay ahead in a "
                    "competitive market."
                ),
                "price": 40000,
            },
            {
                "title": "Software Development",
                "description": (
                    "Custom software development services tailored to your "
                    "business needs. We work closely with you to understand "
                    "your requirements and develop solutions that enhance "
                    "your business operations. Whether you need a desktop "
                    "application, web-based software, or enterprise-level "
                    "systems, we deliver high-quality and scalable software "
                    "solutions."
                ),
                "price": 100000,
            },
            {
                "title": "Third-party Service Integration",
                "description": (
                    "Integration of third-party services and APIs into your "
                    "existing systems to enhance functionality and improve "
                    "business operations. Our team specializes in connecting "
                    "your software with popular services, tools, and "
                    "platforms, such as payment gateways, CRMs, social "
                    "media, and marketing automation systems, allowing "
                    "for a more streamlined and efficient workflow."
                ),
                "price": 60000,
            },
            {
                "title": "Cloud Solutions",
                "description": (
                    "Cloud-based solutions that provide scalability, "
                    "flexibility, and cost savings. We help businesses "
                    "transition to the cloud, implement cloud storage, "
                    "and integrate cloud computing technologies that "
                    "enable remote work and data access. Our team ensures "
                    "the smooth migration of your infrastructure to the "
                    "cloud, with minimal disruption and maximum security."
                ),
                "price": 80000,
            },
            {
                "title": "Cybersecurity",
                "description": (
                    "Comprehensive cybersecurity services to protect your "
                    "organization from digital threats, including hacking, "
                    "data breaches, and malware. We implement robust security "
                    "measures, such as firewalls, encryption, intrusion "
                    "detection systems, and employee training programs. "
                    "Our team ensures that your IT infrastructure is secure "
                    "and compliant with industry standards."
                ),
                "price": 90000,
            },
            {
                "title": "CRM System Development and Implementation",
                "description": (
                    "Design and implementation of custom CRM systems to "
                    "automate and streamline customer relationship "
                    "management. Our CRM solutions help businesses "
                    "manage customer interactions, track sales, and "
                    "improve customer satisfaction. "
                    "We develop tailored CRM systems that integrate with your "
                    "existing processes, enhancing productivity and driving "
                    "long-term customer loyalty."
                ),
                "price": 120000,
            },
        ]

        for service_data in services_data:
            service, create = Service.objects.get_or_create(**service_data)

            self.stdout.write(f"Created service: {service.title}")

        self.stdout.write(
            self.style.SUCCESS("Services created")
        )
