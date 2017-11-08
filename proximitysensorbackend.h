#ifndef PROXIMITYSENSORBACKEND_H
#define PROXIMITYSENSORBACKEND_H

#include <QObject>
#include <QString>

class ProximitySensorBackend : public QObject
{
    Q_OBJECT
    Q_PROPERTY(QString name READ get_name WRITE set_name NOTIFY name_changed)
    Q_PROPERTY(int distance READ get_distance WRITE set_distance NOTIFY distance_changed)

public:
    explicit ProximitySensorBackend(QObject *parent = nullptr);

    QString get_name();
    void set_name(const QString &name);
    int get_distance();
    void set_distance(const int &distance);

signals:
    void name_changed;
    void distance_changed;

private:
    QString m_name;
    int m_distance;
}

#endif // PROXIMITYSENSORBACKEND_H
