#include <proximitysensorbackend.h>

ProximitySensorBackend::ProximitySensorBackend(QObject *parent) : QObject(parent) {

}

QString ProximitySensorBackend::get_name() {
    return m_name;
}

int ProximitySensorBackend::get_distance() {
    return m_distance;
}

void ProximitySensorBackend::set_distance(const int &distance) {
    if (distance == m_distance)
        return;

    m_distance = distance;
    emit distance_changed();
}

void ProximitySensorBackend::set_name(const QString &name) {
    if (name == m_name) {
        return;
    }

    m_name = name;
    emit name_changed();
}
