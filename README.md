\# Cloud-Native GitOps Platform



A production-style cloud-native application demonstrating automated CI/CD, GitOps-based Kubernetes deployments, container security, secret management, and application observability.



\## Architecture



!\[Cloud-Native GitOps Architecture](docs/architecture.png)



\## Project Overview



This project implements an end-to-end DevOps workflow for deploying and monitoring a FastAPI application on Kubernetes.



The platform uses GitHub Actions for CI/CD, GitHub Container Registry for Docker images, Argo CD for GitOps-based deployment, Helm for Kubernetes packaging, Sealed Secrets for secure secret management, and Prometheus/Grafana for observability.



\## Technology Stack



\- \*\*Application:\*\* Python, FastAPI

\- \*\*Testing:\*\* Pytest

\- \*\*Containerization:\*\* Docker

\- \*\*Container Registry:\*\* GitHub Container Registry (GHCR)

\- \*\*CI/CD:\*\* GitHub Actions

\- \*\*Security Scanning:\*\* Trivy

\- \*\*Orchestration:\*\* Kubernetes

\- \*\*Local Kubernetes:\*\* kind

\- \*\*Package Management:\*\* Helm

\- \*\*GitOps:\*\* Argo CD

\- \*\*Secret Management:\*\* Sealed Secrets

\- \*\*Monitoring:\*\* Prometheus

\- \*\*Visualization:\*\* Grafana

\- \*\*Version Control:\*\* Git, GitHub



\## CI/CD Workflow



```text

Developer

&#x20;   |

&#x20;   v

&#x20; GitHub

&#x20;   |

&#x20;   v

GitHub Actions

&#x20;   |

&#x20;   +-- Run Pytest

&#x20;   |

&#x20;   +-- Build Docker Image

&#x20;   |

&#x20;   +-- Scan Image with Trivy

&#x20;   |

&#x20;   +-- Push Image to GHCR

&#x20;   |

&#x20;   +-- Update Helm Image Tag

&#x20;   |

&#x20;   v

&#x20;GitOps Repository

&#x20;   |

&#x20;   v

&#x20; Argo CD

&#x20;   |

&#x20;   v

&#x20;Kubernetes

